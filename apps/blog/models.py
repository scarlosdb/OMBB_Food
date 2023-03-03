from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    pic = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    private = models.BooleanField()

    # def save(self, *args, **kwargs):
    #     # self.slug = slugify(self.blog_title)
    #     super().save(*args, **kwargs)


# def blog_pre_save(sender, instance, *args, **kwargs):
#     if instance.slug in None:
#         instance.slug = slugify(instance.blog_title)
#
#
# pre_save.connect(blog_pre_save, sender=Blog)
#
#
# def blog_post_save(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.slug = "this is a test"
#         instance.save()
#
#
# post_save.connect(blog_post_save, sender=Blog)
#

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
