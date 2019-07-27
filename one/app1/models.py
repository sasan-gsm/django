from django.db import models
from organizer.models import Tag, Startup
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, help_text='A label for URL config', unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def get_absolute_url(self):
        return reverse('app1_post_detail', kwargs={'year': self.pub_date.year,'month': self.pub_date.month,'slug': self.slug})

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

