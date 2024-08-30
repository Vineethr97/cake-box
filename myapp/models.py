from django.db import models


class Cakes(models.Model):
    name=models.CharField(max_length=250)
    flavour=models.CharField(max_length=200)
    shape=models.CharField(max_length=230)
    price=models.FloatField()
    weight=models.CharField(max_length=200)
    layer=models.CharField(max_length=200)
    description=models.CharField(max_length=2550)
    pic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name

 