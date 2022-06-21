from os import getenv

from redis import asyncio as aioredis


redis = aioredis.from_url("redis://127.0.0.1:6379")