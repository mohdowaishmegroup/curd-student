from rest_framework import serializers
from.models import *
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        exclude=('created_at','updated_at','is_deleted','deleted_at')