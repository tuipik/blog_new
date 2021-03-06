# Generated by Django 2.1.7 on 2019-03-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190324_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Можливість редагувати'),
        ),
    ]
