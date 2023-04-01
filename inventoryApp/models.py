from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.
class item(models.Model):
    productName = models.CharField(max_length=20)
    brandName = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=20)
    supplier = models.CharField(max_length=20)
    supplier_contact_number = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    acquired_date = models.DateField()
    expiry_date = models.DateField()

#    acquired_date = models.CharField(max_length=10, validators=[MaxLengthValidator(10),MinLengthValidator(10)])
#    expiry_date = models.CharField(max_length=10, validators=[MaxLengthValidator(10),MinLengthValidator(10)])



