import re

from schemas import Extra


def get_links(text: str):
    """Находит ссылки в тексте"""
    pattern = r'(https?://[^\s]+)'
    links = re.findall(pattern, text)

    result = []
    for link in links:
        result.append(
            Extra(text=link, offset=text.find(link), length=len(link))
        )

    return result


def get_hashtags(text: str):
    """Находит хештеги в тексте"""
    pattern = r'(#[\wа-яА-Я]+)'
    hashtags = re.findall(pattern, text)

    result = []
    for hashtag in hashtags:
        result.append(
            Extra(text=hashtag, offset=text.find(hashtag), length=len(hashtag))
        )

    return result


def get_reference(text: str):
    """Находит упоминания в тексте"""
    pattern = r'(@[\wа-яА-Я]+)'
    references = re.findall(pattern, text)

    result = []
    for reference in references:
        result.append(
            Extra(text=reference, offset=text.find(reference), length=len(reference))
        )

    return result


def get_extra(text: str):
    """Находит в тексте экстра-данные: ссылки, упоминания и т.д."""
    extra = []

    extra += get_links(text)
    extra += get_hashtags(text)
    extra += get_reference(text)

    return extra