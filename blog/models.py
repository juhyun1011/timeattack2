from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    class Meta:
        db_table = "Category"

    category = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)

class ArticleModel(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=256)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)



