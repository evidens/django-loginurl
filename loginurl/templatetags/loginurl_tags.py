from django import template
from loginurl.utils import create
from django.core.urlresolvers import reverse

register = template.Library()
@register.simple_tag
def create_login_url(user):
    key = create(user)

    return reverse('loginurl-login', args=[key.key])
