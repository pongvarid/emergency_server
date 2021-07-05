from django.contrib import admin

from backend.models import Exercise,Language, Course, Senses, Vocabulary
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    # filter_horizontal = ['video']
    pass



admin.site.register(Exercise)
admin.site.register(Course,CourseAdmin)
admin.site.register(Language)
admin.site.register(Senses)
admin.site.register(Vocabulary)
