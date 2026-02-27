from django.urls import path
from website.views import *

app_name='website'

urlpatterns = [
    path('', index, name='index'),
    path('certificate/', certificate, name='certificate'),
    path('projects/', projects, name='projects'),
    path('appreciation/', appreciation, name='appreciation'),
   
    path('contact/', contact_view, name='contact'),
]
    




# urlpatterns = [
#     path('', contact_view, name='contact'),
# ]