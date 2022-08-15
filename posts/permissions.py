from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticate users only ca see list view
        if request.user.is_authenticated:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):

        # Read permission to all
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write (post/put) to author only
        return obj.author == request.user