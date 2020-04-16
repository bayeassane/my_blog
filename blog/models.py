from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('nom de catégorie', max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    created_at = models.DateTimeField('date de création', auto_now_add=True)
    updated_at = models.DateTimeField('date de mise à jour', auto_now=True)
    title = models.CharField('titre', max_length=50)
    content = models.TextField("contenu de l'article")
    image = models.ImageField('photo', upload_to="images", null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



