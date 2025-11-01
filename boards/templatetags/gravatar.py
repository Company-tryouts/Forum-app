import hashlib
from urllib.parse import urlencode

from django import template

register = template.Library()


@register.filter
def gravatar(user):
    # Safely handle users with no email
    email = (user.email or "").strip().lower().encode("utf-8")

    params = {
        "d": "mp",  # 'mp' = modern placeholder, replaces old 'mm'
        "s": "256",
    }

    hash_ = hashlib.md5(email).hexdigest()
    url = f"https://www.gravatar.com/avatar/{hash_}?{urlencode(params)}"
    return url
