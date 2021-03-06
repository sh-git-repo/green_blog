from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    blog_date = models.DateField(auto_now_add=True)
    usr = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
