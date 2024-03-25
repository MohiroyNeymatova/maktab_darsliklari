from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    is_class = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    year = models.IntegerField()
    memory = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books/')
    description = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.name

