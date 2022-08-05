from rest_framework.serializers import ModelSerializer, IntegerField, Serializer
from .models import Sheet


class SheetSerializer(ModelSerializer):
    """This serializer is used to process sheet data for the sending through API view
    """
    class Meta:
        model = Sheet
        fields = '__all__'


class TotalSerializer(Serializer):
    total_sum = IntegerField()