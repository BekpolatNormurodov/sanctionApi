from rest_framework.generics import *
from api.models import *
from .serializers import *
from rest_framework.generics import *

# Test Api
class TestApiView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = Testserializer

class TestApiCreate(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = Testserializer

class TestApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = Testserializer