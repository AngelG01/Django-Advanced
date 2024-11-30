from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,
                               related_name='recipes')

    def __str__(self):
        return self.title
