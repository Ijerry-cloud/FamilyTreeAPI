from rest_framework import serializers
from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        exclude = ["user"]
        model = Profile
        
