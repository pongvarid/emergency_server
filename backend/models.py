from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='lang_icon/', null=True, blank=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='course_icon/', null=True, blank=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.name)



class Vocabulary(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    tranword = models.CharField(max_length=255)
    sound = models.FileField(upload_to='sound/', null=True, blank=True, verbose_name="Sound")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Senses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    accent = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='Sense_icon/', null=True, blank=True, verbose_name="Image")
    enabled_link = models.BooleanField(default=True)
    video = models.FileField(upload_to='video', null=True, blank=True, verbose_name="Video File")
    video_link = models.TextField( null=True, blank=True, verbose_name="Video File")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.title)

class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    accent = models.ForeignKey(Language, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    a = models.TextField(null=True, blank=True)
    b = models.TextField(null=True, blank=True)
    c = models.TextField(null=True, blank=True)
    d = models.TextField(null=True, blank=True)
    ans = models.CharField(max_length=255,choices=[('a','a',), ('b','b'), ('c','c'), ('d','d')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.question)





