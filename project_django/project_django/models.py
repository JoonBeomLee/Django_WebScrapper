from django.db import models

class scrapper_result(models.Model):
    search_word = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    