from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

#run bash command
@api_view(['GET', 'POST'])
def myapi(request):
	return Response(os.popen("date").read())
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/$', myapi),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]