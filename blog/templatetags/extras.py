from django import template

register = template.Library()
@register.inclusion_tag('platform/templatetags/paginat')
def dict_unpack(dict_post, var):
	return {'title' : dict_post[var]}

def unpack_title(posts, var):
	return dict_unpack(posts[var], 'title')

