from django import template

register = template.Library()


@register.filter
def first_letter(user):
    if user.first_name:
        return user.first_name[0].upper()
    return 'A'
