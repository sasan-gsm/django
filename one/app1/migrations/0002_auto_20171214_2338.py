# Generated by Django 2.0 on 2017-12-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Startup'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='A label for URL config', max_length=60, unique_for_month='pub_date'),
        ),
    ]
