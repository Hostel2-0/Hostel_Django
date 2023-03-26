
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Towns(models.Model):
    name= models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='towns', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'towns'
        verbose_name_plural = 'townss'

    # def get_url(self):
    #      return reverse('hostels_by_towns', args=[self.slug])

    def __srt__(self):
        return self.name

class Hostel(models.Model):
    name= models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    towns = models.ForeignKey(Towns, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='hostel', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'hostel'
        verbose_name_plural = 'hostels'
    
    def get_url(self):
        return reverse('hostels_detail', args=[self.towns.slug, self.slug])

    def __srt__(self):
        return self.name
    
class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)
    surname = models.CharField(max_length=250, null= True)
    phonenumber = models.CharField(max_length=250, unique=True,null= True)
    medicalnumber = models.CharField(max_length=100, null= True)
    location = models.CharField(max_length=250, null= True)
    university = models.CharField(max_length=100, null= True)
    course = models.IntegerField(null= True)
    parentname = models.CharField(max_length=70, null= True)
    parentlastname = models.CharField(max_length=70, null= True)
    parentsurname = models.CharField(max_length=70,null= True) 
    parentnumber = models.CharField(max_length=70,null= True)

    def unicode(self):
        return self.user
        