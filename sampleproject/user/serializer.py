from .models import *
from rest_framework import serializers


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields =('start_time','end_time')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ActivityPeriodAndUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
