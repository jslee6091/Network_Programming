from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for this alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'

        # descending(내림차순)
        ordering = ('-modify_date',)

        # ascending(오름차순) 은 'modify_date' 로 하면 됨
    
    
    def get_absolute_url(self):
        # http://localhost:8000/blog/post/daily
        return reverse('blog:post_detail', args=(self.slug,)) # args는 tuple인데 뒤에 ,를 붙여야 함

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

