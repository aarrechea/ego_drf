# Imports
from django.db import transaction
from apps.abstract.serializers import AbstractSerializer
from apps.car.models import Car, CarFeature
from apps.features.models import Feature
from apps.features.serializers import FeatureSerializer



# Car serializer
class CarSerializer(AbstractSerializer):    
    feature = FeatureSerializer(read_only=True, many=True)
    
    
    def create(self, validated_data):
        
        print("\nEnter create serializer")
        
        features = self.initial_data['features']
        locations = self.initial_data['locations']
                        
        listInstances = []        
        array = []
        
        # Get the feature object from the front end data
        for feature in features:            
            listInstances.append(Feature.objects.get(id=feature))
            
            
        print("\nBefore try - list instances: ", listInstances)
            
        try:            
            with transaction.atomic():                
                car = Car.objects.create(**validated_data)
                
                print("\nInside try - Car: ", car)
                
                for index, item in enumerate(listInstances):
                    car_feature = CarFeature(
                        car = car,
                        feature = item,
                        location = locations[index]
                    )
                    array.append(car_feature)
                
                print("\nAfter for - car_feature: ", car_feature)
                
                
                CarFeature.objects.bulk_create(array)
                
            return car
        
        except Exception as e:            
            return e
                        
    
    def to_representation(self, instance):        
        # Car
        rep = super().to_representation(instance) 
        
        # Car features   
        objs = CarFeature.objects.filter(car=rep['id'])
        
        features = []
        locations = []
        
        # Features from Car Features model
        for obj in objs:            
            features.append(Feature.objects.get(id=obj.feature.id))
            locations.append(obj.location)            
                                                
        rep['features'] = FeatureSerializer(features, many=True).data
        rep['locations'] = locations
        
        return rep
    
    
    class Meta:
        model = Car
        fields = [
            'id',
            'created',
            'updated',
            'manufacturer',
            'model',
            'designation',                        
            'year',
            'type',
            'price',
            'photo',
            'feature',
        ]
        
        
