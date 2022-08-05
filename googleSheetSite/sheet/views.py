from django.shortcuts import render
from .models import Sheet
from . import tasks
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SheetSerializer, TotalSerializer


def SPA(request):
    """This view renders the SPA showing the initial table
    """
    values = Sheet.objects.all()
    ctx = {'values': values}
    return render(request, 'sheet/SPA.html', ctx)


@api_view(["GET"])
def renew_sheet(request):
    """This view is created for google sheets script that makes a request to this api when the sheet has been changed
    in order for cellery to initiate new fetch from the google sheets. For this to work there must be a constant adress
    for google sheet to make a request
    """
    tasks.save_sheet_in_the_db.delay()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_sheet(request):
    """This API view provides client with data from the Google Sheets
    """
    sheet = Sheet.objects.all().order_by('number_in_table')
    serializer = SheetSerializer(sheet, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_total(request):
    """This API view provides client with data from the Google Sheets
    """
    total = Sheet.total_sum()
    serializer = TotalSerializer(data={'total_sum': total}, many=False)
    serializer.is_valid()
    return Response(serializer.data)