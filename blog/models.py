from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, default=None)

	
	def __str__(self):
	    return self.title


	def snippet(self):
	  return self.body[:50] + '....'
	

 









#class Post(models.Model):
    #name = models.CharField(max_length=100)
    #tagline = models.TextField()

    #def __str__(self):
        #return self.name

#class Author(models.Model):
    #name = models.CharField(max_length=200)
    #email = models.EmailField()

    #def __str__(self):
        #return self.name

#class Entry(models.Model):
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #headline = models.CharField(max_length=255)
    #body_text = models.TextField()
    #pub_date = models.DateField()
    #mod_date = models.DateField()
    #authors = models.ManyToManyField(Author)
    #n_comments = models.IntegerField()
    #n_pingbacks = models.IntegerField()
    #rating = models.IntegerField()

    #def __str__(self):
        #return self.headline



      