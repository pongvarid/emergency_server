from django.contrib import admin

from backend.models import Exercise, Accent, Course, Senses, Vocabulary
# Register your models here.

class AccentAdmin(admin.ModelAdmin):
    filter_horizontal = ['course']



admin.site.register(Exercise)
admin.site.register(Course)
admin.site.register(Accent, AccentAdmin)
admin.site.register(Senses)
admin.site.register(Vocabulary)
