from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'bucketlists')
