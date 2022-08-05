from django.urls import path

from . import views

app_name = 'sheet'
urlpatterns = [
    path('', views.SPA, name='SPA'), #main page
    #path('api/sheet_edited', views.renew_sheet, name="renewed"),   This URL is for unused - more info in views
    path('api/sheet', views.get_sheet, name='get_sheet'), #api for fetching data from db
    path('api/total', views.get_total, name='get_total')
]