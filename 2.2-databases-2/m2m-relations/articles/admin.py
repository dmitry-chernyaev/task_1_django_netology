from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Считаем количество основных тегов
        main_tags_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') and not form.cleaned_data.get('DELETE', False):
                main_tags_count += 1

        # Проверяем условия
        if main_tags_count == 0:
            raise ValidationError('У статьи должен быть хотя бы один основной тег')
        elif main_tags_count > 1:
            raise ValidationError('У статьи может быть только один основной тег')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']