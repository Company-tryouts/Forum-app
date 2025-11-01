from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_user_count():
    return User.objects.count()
