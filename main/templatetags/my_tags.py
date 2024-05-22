from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_year():
    return datetime.now().year


@register.simple_tag(takes_context=True)
def current_domain(context):
    request = context['request']
    return request.get_host()


@register.simple_tag(takes_context=True)
def active_menu(context):
    request = context['request']
    current_url = request.path
    menu_url = current_url.split('/')[1]
    menu_list = {
        'about': 'About Me',
        'blog': 'Blog',
        'portfolio': 'Portfolio',
        'contact': 'Contact Me',
    }

    for key, value in menu_list.items():
        if current_url == '/':
            return 'Home'
        elif key == menu_url:
            return value


@register.simple_tag(takes_context=True)
def inactive_menus(context):
    request = context['request']
    current_url = request.path
    menu_url = current_url.split('/')[1]

    menu_list = {
        'about': 'About Me',
        'blog': 'Blog',
        'portfolio': 'Portfolio',
        'contact': 'Contact Me',
    }
    if current_url == '/':
        return menu_list
    for key, value in menu_list.items():
        if menu_url == key:
            menu_list.pop(key)
            break
    return menu_list
