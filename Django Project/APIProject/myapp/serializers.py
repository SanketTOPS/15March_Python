from rest_framework import serializers
from .models import studInfo

class StudSerial(serializers.ModelSerializer):
    class Meta:
        model=studInfo
        fields='__all__'
