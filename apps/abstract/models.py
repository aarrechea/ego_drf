# Imports
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404



# Abstract manager
class AbstractManager(models.Manager):
    def get_object_by_id(self, id):
        try:
            instance = self.get(id=id)            
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        
        
        
# Abstract model        
class AbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = AbstractManager()
    

    # Meta
    class Meta:
        abstract = True