from django.db import models

# Create your models here.
class Calibre(models.Model):
     
    id= models.AutoField(primary_key=True)
    name= models.CharField(blank=False,max_length=20)

    def __str__(self):
        return self.name

class Ammo(models.Model):

    id = models.AutoField(primary_key=True)
    name= models.CharField(blank=False,max_length=20)
    calibre = models.ForeignKey(to=Calibre,blank=False,on_delete=models.CASCADE)
    imagen = models.ImageField(blank=False)

    def __str__(self):
        return f'{self.calibre} {self.name}'