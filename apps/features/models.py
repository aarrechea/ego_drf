# Imports
from django.db import models
from apps.abstract.models import AbstractModel



# File will be uploaded to MEDIA_ROOT/features_<id>/<filename>
def feature_directory_path(instance, filename):
    if instance:
        return "feature_{0}/{1}".format(instance.id, filename)
    else:
        feature = Feature.objects.latest('id')    
        return "feature_{0}/{1}".format(feature.id, filename)



# Feature model
class Feature(AbstractModel):
    photo = models.ImageField(null=True, blank=True, upload_to=feature_directory_path)
    designation = models.CharField(max_length=20, default='None', blank=True, null=True)
    title = models.CharField(max_length=70)        
    description = models.TextField(max_length=400)
    
    def __str__(self):
        return self.title
    
    


