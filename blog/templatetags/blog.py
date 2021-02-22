from django import template
from blog.models import Category, Tag

register = template.Library()

@register.inclusion_tag("blog/category_and_tag_list.html")
def create_category_and_tag_list():
    return {
        "category_list": Category.objects.all(),
        "tag_list": Tag.objects.all(),
    }

@register.inclusion_tag("blog/search_form.html")
def create_search_form(request):
    form = PostSearchForm()
    return {"form":form}

