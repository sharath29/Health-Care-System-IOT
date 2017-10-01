# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here
from .models import Question
from .models import Choice,Signup,Patient

class ChoiceInline(admin.StackedInline):
   model = Choice
   extra = 3


class QuestionAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,               {'fields': ['question_text']}),
       ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   ]
   inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Signup)
admin.site.register(Patient)

