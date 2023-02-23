from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Page, Image


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Page
        fields = ['title', 'featured_image', 'description', 'call_to_action', 'slug', 'user']

    def create(self, validated_data):
    # Set the user field to the currently authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image']