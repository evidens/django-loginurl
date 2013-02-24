from django import template
from loginurl.utils import create

register = template.Library()
@register.simple_tag
def create_login_url(user):
    key = create(user)
    url = '/loginurl/%s' % key.key

    return url    
