from django.contrib import admin
from . models import Category,StudyMaterials,HomeWorkQtn,HomeWork
from .models import Poll, Choice

# Register your models here.

class ChoiceAdmin(admin.StackedInline):
    model=Choice
class PollAdmin(admin.ModelAdmin):
    inlines=[ChoiceAdmin]



admin.site.register(Category)
admin.site.register(StudyMaterials)
admin.site.register(HomeWorkQtn)
admin.site.register(HomeWork)
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)