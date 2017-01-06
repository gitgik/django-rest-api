from rest_framework.permissions import BasePermission
from .models import Bucketlist

class OwnerOrReadOnly(BasePermission):
    """Custom permission class to allow bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Bucketlist):
            return obj.bucketlist.owner == request.user
        return obj.owner == request.user
