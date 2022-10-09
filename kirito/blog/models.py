from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField



class Category(MPTTModel):
    name = models.CharField(max_length=100, help_text="max length 100s")
    slug = models.SlugField(max_length=100, help_text="max length 100s")
    
    parent = TreeForeignKey(
        'self', 
        related_name='children', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    def __str__(self):
        return self.name

    class MTTPMeta:
        order_insertion_by = ['name']



class Tag(models.Model):    
    name = models.CharField(max_length=100, help_text="max length 100s")
    slug = models.SlugField(max_length=100, help_text="max length 100s")
    
    def __str__(self):
        return self.name




class Post(models.Model):
    author = models.ForeignKey(User , related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="max length 200s")
    image = models.ImageField(upload_to='articles/')
    text = models.TextField(max_length=3000, help_text="max length 200s")
    category = models.ForeignKey(Category, related_name="post", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name="post")
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='', help_text="max length 200s", unique=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_intopost(self):
        return self.intopost.all()


class IntoPost(models.Model):
    name = models.CharField(max_length=100, help_text="max length 100s")
    about = models.TextField()
    allpost = RichTextField()
    author = models.CharField(max_length=50, default='', help_text="max length 50s")
    country = models.CharField(max_length=50, default='', help_text='max length 50s')
    time_to_read = models.CharField(max_length=3, default='', help_text="add only numbers")
    sources = RichTextField(max_length=500, default='', help_text='max length 200s')
    header = models.CharField(max_length=200, default='', help_text='max length 200s')
    under_article = models.CharField(max_length=20, default='', help_text="max length 20s")

    def words(self):
        return len(self.allpost.split())

    post = models.ForeignKey(
        Post,
        related_name="intopost",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    

class Comment(models.Model):
    name = models.CharField(max_length=50, help_text="max length 50s")
    email = models.CharField(max_length=100, help_text="max length 100s")
    website = models.CharField(max_length=150, help_text="max length 150s")
    message = models.CharField(max_length=500, help_text="max length 500s")
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
