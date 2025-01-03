# Imports
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.abstract.models import AbstractModel
from apps.features.models import Feature



# Car manufacturers
CAR_MANUFACTURERS = (
    (1, "Toyota"),
    (2, "Renault"),
    (3, "Volkswagen"),
    (4, "Citroen"),
)



# Car types
CAR_TYPE = (
    (1,'Auto'),
    (2,'Pickup'),
    (3,'Comercial'),
    (4,'Suv'),
    (5,'Crossover'),
)



# Locations
LOCATIONS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
)



# File will be uploaded to MEDIA_ROOT/car_<id>/<filename>
def car_directory_path(instance, filename):
    if instance.id:
        return "cars/car_{0}/{1}".format(instance.id, filename)
    else:
        car = Car.objects.latest('id')    
        return "cars/car_{0}/{1}".format(car.id, filename)



# Car model
class Car(AbstractModel):
    manufacturer = models.IntegerField(choices=CAR_MANUFACTURERS)
    model = models.CharField(max_length=40)
    designation = models.CharField(max_length=40, blank=True, null=True)
    year = models.IntegerField(validators=[
            MaxValueValidator(2050),
            MinValueValidator(1990)
        ])
    type = models.IntegerField(choices=CAR_TYPE, default=1)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    photo = models.ImageField(null=True, blank=True, upload_to=car_directory_path)
    features = models.ManyToManyField(Feature, through='CarFeature')
    
    
    @property
    def name_model(self):
        return f"{self.get_manufacturer_display()} {self.model} {self.designation}"
    
    
            
# Linking many to many table    
class CarFeature(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    location = models.IntegerField(choices=LOCATIONS, default=1) # location of the photo in the page


