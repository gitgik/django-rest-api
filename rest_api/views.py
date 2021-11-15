from rest_framework import generics
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
