from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, ArticleWithSection


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        section_list = []
        count = 0
        for form in self.forms:
            section = form.cleaned_data['section']
            is_main = form.cleaned_data['is_main']
            if section in section_list:
                raise ValidationError('ОШИБКА: повторяются разделы')
            elif is_main:
                count += 1
                if count > 1:
                    raise ValidationError('ОШИБКА: больше одного главного раздела')
            section_list.append(section)
        if count == 0:
            raise ValidationError('ОШИБКА: не выбран главный раздел')
        return super().clean()


class SectionInLine(admin.TabularInline):
    model = ArticleWithSection
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        SectionInLine
    ]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
