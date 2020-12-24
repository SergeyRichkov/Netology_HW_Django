from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    relation_list = Article.objects.all().prefetch_related('article__section').order_by('-published_at')

    context = {
        'relation_list': relation_list,
    }
    return render(request, template, context)


