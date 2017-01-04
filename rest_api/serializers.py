from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
