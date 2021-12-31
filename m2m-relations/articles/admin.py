from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope

# проверяем на один основной тег
class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        true_count = 0
        form_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data:
                form_count += 1
                if 'is_main' in form.cleaned_data and form.cleaned_data['is_main']:
                    true_count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        else:
            if true_count != 1 and form_count > 0:
                raise ValidationError('Должен быть один основной тэг')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 3
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [
        ArticleScopeInline,
    ]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass