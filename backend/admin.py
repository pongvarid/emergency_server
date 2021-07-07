from django.contrib import admin

from backend.models import Exercise,Language, Course, Senses, Vocabulary
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','created_at' )
    search_fields = ['name', ]
    pass

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('course', 'accent', 'question', 'created_at')
    list_filter = ('course', 'accent',)
    search_fields = ['question', ]
    pass

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','created_at' )
    search_fields = ['name', ]
    # filter_horizontal = ['video']
    pass

class SensesAdmin(admin.ModelAdmin):
    list_display = ('course', 'accent', 'title', 'created_at')
    list_filter = ('course','accent',)
    search_fields = ['title',]
    pass


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('course','word','tranword','created_at' )
    list_filter = ('course',)
    search_fields = ['word', ]
    pass

admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Senses,SensesAdmin)
admin.site.register(Vocabulary,VocabularyAdmin)
