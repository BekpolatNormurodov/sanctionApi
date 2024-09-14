from rest_framework import serializers
from api.models import *

class Testserializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','title')