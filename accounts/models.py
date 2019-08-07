from django.db import models


class Inputform(models.Model):
    title = models.TextField()
    product_name = models.TextField()
    location = models.TextField()
    person_num = models.TextField()
    price = models.TextField()
    link = models.TextField()
    account = models.TextField()
    date_limit = models.DateTimeField('date published')
    explanation = models.CharField(max_length=300)
    photo = models.FileField(upload_to='inputphotos/', blank=True, null=True)
    
