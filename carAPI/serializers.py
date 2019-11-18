from rest_framework import serializers
from .models import Car, Maker, Color


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'maker', 'model', 'fuel']


class CarDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color', 'rgb']


class MakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maker
        fields = '__all__'
