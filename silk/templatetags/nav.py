from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def navactive(request, urls, url_arg=None):
    path = request.path
    if url_arg:
    	urls = [reverse(url, args=[url_arg]) for url in urls.split()]
    else:
    	urls = [reverse(url) for url in urls.split()]
    if path in urls:
        cls = "menu-item-selected"
        return cls
    return ""
