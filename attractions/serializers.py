from rest_framework import serializers
from attractions.models import Attractions, CATEGORY_CHOICES
from django.contrib.auth.models import User


class AttractionsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attractions
        fields = ['id', 'title', 'category', 'description', 'cover_image', 'country', 'city', 'owner']

    def create(self, validated_data):
        # Create and return a new `Attractions` instance, given the validated data.
        return Attractions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing `Attractions` instance , given the validated  data.
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    attractions = serializers.PrimaryKeyRelatedField(many=True, queryset=Attractions.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'attractions']
