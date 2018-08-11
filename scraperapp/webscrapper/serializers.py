from rest_framework import serializers
from . models import subjectModel, articleModel, authorModel

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjectModel
        fields = ('name', 'color')

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = articleModel
        fields = '__all__'

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = authorModel
        fields = '__all__'
