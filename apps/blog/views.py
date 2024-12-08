from django.shortcuts import render

from .models import Publication, Category, Tag


def home(request):
    context = {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'publications': Publication.objects.all().order_by('-created')[:5]
    }
    return render(request=request, template_name='index.html', context=context)
