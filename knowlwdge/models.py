from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Knoeledge(models.Model):
    class Meta:
        verbose_name = _("Knowledge")
        verbose_name_plural = _("Knowledge")
    name = models.CharField(verbose_name="ชื่อ",max_length=255)
    image = models.ImageField(null=True,blank=True,verbose_name="ภาพหัวเรื่อง")
    detail = models.TextField(verbose_name="รายระเอียด")
    image1 = models.ImageField(null=True, blank=True,verbose_name="ภาพประกอบ 1")
    image2 = models.ImageField(null=True, blank=True,verbose_name="ภาพประกอบ 2")
    image3 = models.ImageField(null=True, blank=True,verbose_name="ภาพประกอบ 3")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
