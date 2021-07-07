# Generated by Django 3.2.4 on 2021-07-07 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Knoeledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ชื่อ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ภาพหัวเรื่อง')),
                ('detail', models.TextField(verbose_name='รายระเอียด')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ภาพประกอบ 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ภาพประกอบ 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ภาพประกอบ 3')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'A (แอปพลิเคชัน) องค์ความรู้',
                'verbose_name_plural': 'A (แอปพลิเคชัน) องค์ความรู้',
            },
        ),
    ]