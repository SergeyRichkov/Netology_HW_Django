from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=50, )
    articles = models.ManyToManyField(Article,  through='ArticleWithSection', related_name='section')


    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


    def __str__(self):
        return self.name


class ArticleWithSection(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section_id')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['section__name']


