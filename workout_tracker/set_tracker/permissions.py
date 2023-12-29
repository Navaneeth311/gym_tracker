from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it"""
    #Params:  request is the HTTP request that's being processed, 
    #view is the DRF view that's handling the request, and obj is the object that the request is operating on.
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the Tracker.
        return obj.owner == request.user
    """if the owner of the obj is the same as the user making the request (request.user). 
    If they are the same, it returns True, granting permission. 
    If they're not the same, it returns False, denying permission"""
    