from django.urls import path

from . import views

app_name = 'sheet'
urlpatterns = [
    path('', views.SPA, name='SPA'),
    #path('api/sheet_edited', views.renew_sheet, name="renewed"),   This URL is for unused - more info in views
    path('api/sheet', views.get_sheet, name='get_sheet')
]