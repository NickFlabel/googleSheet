from rest_framework.serializers import ModelSerializer
from .models import Sheet


class SheetSerializer(ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'