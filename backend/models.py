from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='course_images/', null=True, blank=True, verbose_name="Image")

    def __str__(self):
        return '{}'.format(self.title)


class Accent(models.Model):
    course = models.ManyToManyField(Course)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='accent_images', null=True, blank=True, verbose_name="Image")

    def __str__(self):
        return '{}'.format(self.title)

class Vocabulary(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    accent = models.ForeignKey(Accent, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    tranword = models.CharField(max_length=255)
    sound = models.FileField(upload_to='sound/', null=True, blank=True, verbose_name="Sound")

class Senses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    accent = models.ForeignKey(Accent, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='video_images/', null=True, blank=True, verbose_name="Image")
    video = models.FileField(upload_to='video', null=True, blank=True, verbose_name="Video File")

    def __str__(self):
        return '{}'.format(self.title)

class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    accent = models.ForeignKey(Accent, on_delete=models.CASCADE)
    question = models.TextField(max_length=5000)
    a = models.CharField(max_length=500)
    b = models.CharField(max_length=500)
    c = models.CharField(max_length=500)
    d = models.CharField(max_length=500)
    ans = models.CharField(max_length=255,choices=[('a','a',), ('b','b'), ('c','c'), ('d','d')])




