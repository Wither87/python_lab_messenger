from fastapi import FastAPI
from endpoints.user import router as user_router
from endpoints.chat import router as chat_router
from endpoints.message import router as message_router
from endpoints.login import router as login_router
import uvicorn

app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)
app.include_router(login_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        debug=True,
    )