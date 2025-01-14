""" Imports """
from rest_framework.permissions import BasePermission, SAFE_METHODS



""" User permission class """
class UserPermission(BasePermission):            
    basenameArray = ['user', 'car', 'feature']
            
    # works in the object level
    def has_object_permission(self, request, view, obj):        
        if request.user.is_anonymous:            
            return request.method in SAFE_METHODS # get, options, and head
                
        if view.basename in self.basenameArray:            
            # Any user that has permission could view the element
            if request.method == 'GET':
                return True                        
            else:                    
                if obj.user_creator.id != request.user.id:
                    return False                                    
            return bool(request.user and request.user.is_authenticated)        
        return False
    
    
    # works in the overall endpoint
    def has_permission(self, request, view):        
        if view.basename in self.basenameArray:
            if request.user.is_anonymous:                
                return False # request.method in SAFE_METHODS            
            return bool(request.user and request.user.is_authenticated)
        
        return False
            






