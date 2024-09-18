from rest_framework import serializers
from api.models import *
from config import settings

class Testserializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','title', 'logo', 'pdf', 'pdf_url')

    def get_pdf_url(self, obj):
        if obj.image:
            pdf_url = f"{settings.MEDIA_URL}{obj.image}"
            pdf_fied_url = f"{settings.BASE_URL}/sanctionApi{pdf_url}"
            return pdf_fied_url
        return None