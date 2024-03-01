from .models import Review
from rest_framework import serializers

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields= '__all__'