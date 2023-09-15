from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.CharField(max_length=64)

    def __str__(self):
        return self.Category
    
class Classes(models.Model):
    class_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=255)
    class_year = models.IntegerField()
    class_credit = models.IntegerField()
    semester = models.IntegerField()
    class_category = models.ForeignKey(Category, on_detele=models.CASCADE)

    def __str__(self):
        return self.class_name
