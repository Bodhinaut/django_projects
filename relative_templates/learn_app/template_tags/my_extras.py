from django import template

register = template.Library()
# can also do the above with decorators, lets do it..

@register.filter(name='cut')

def cut(arg):
	"""cuts out all values of arg from the string"""
	return value.replace(arg, '')

# register.filter('cut', cut)
# passing in a function into a function call, so we will use
# a decorator 
# pass as string what you want to call it, and pass in name of funciton
