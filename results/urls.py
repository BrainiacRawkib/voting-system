from django.urls import path
from .views import *

app_name = 'results'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lga-results/', LGAResultListView.as_view(), name='lga-results'),
    path('summed-results/<slug:name>/', LGATotalResult.as_view(), name='summed-results'),
    path('pu-results/', PUResultListView.as_view(), name='pu-results'),
]

