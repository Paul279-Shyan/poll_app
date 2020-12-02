from django.contrib import admin
from .models import *


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
