from rest_framework import serializers
from .models import SetTracker
from django.contrib.auth.models import User


class SetTrackerSerializer(serializers.ModelSerializer):
    owner =  serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = SetTracker
        fields = ['id', 'day', 'sets', 'comments', 'owner']


class UserSerializer(serializers.ModelSerializer):
    set_tracker = serializers.PrimaryKeyRelatedField(many=True, queryset=SetTracker.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'set_tracker']

    """Model Serializers will automatically add the create and update flow unlike the Serializer class"""

# class SetTrackerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     day = serializers.CharField(required=True, max_length=100, allow_blank=False)
#     sets = serializers.IntegerField(min_value=3)
#     comments = serializers.CharField(allow_blank=True, max_length=500)

#     # How create and Update is performed when serializer.save() is called

#     def create(self, validated_data):
#         return SetTracker.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.day = validated_data.get('day', instance.day)
#         instance.sets = validated_data.get('sets', instance.sets)
#         instance.comments = validated_data.get('comments', instance.comments)
#         instance.save()
#         return instance