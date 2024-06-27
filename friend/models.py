from django.db import models

# Create your models here.
class Hello(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='hello'
        verbose_name_plural='hellos'
