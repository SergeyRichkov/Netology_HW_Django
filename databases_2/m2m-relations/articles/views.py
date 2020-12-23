from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    relation_list = Article.objects.all().prefetch_related('article__section').\
        order_by('-published_at')



    # for r  in relation_list:
    #     f = r.section.all().order_by('name')
    #     print(f)
    #     for k in f:
    #         print(k)
    #     print('____________')


    context = {
        'relation_list': relation_list,
    }
    return render(request, template, context)


