from django import template
import math

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg

@register.filter(name='divide')
def divide(value, arg):
    try:
        return value / arg
    except (ValueError, ZeroDivisionError):
        return None

@register.filter(name='absolute')
def absolute(value):
    return abs(value)

@register.filter(name='floor')
def floor(value):
    return math.floor(value)

@register.filter(name='ceil')
def ceil(value):
    return math.ceil(value)

@register.filter(name='round')
def round_filter(value, arg=0):
    return round(value, arg)


@register.filter(name='div')
def div(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return ''


@register.filter(name='mul')
def mul(value, arg):
    return value * arg
