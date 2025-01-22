from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = 'customers'
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'