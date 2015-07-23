from django.conf.urls import include, url
from calendarium import views as calendarium
from . import views


urlpatterns = [
    url(r'', include('calendarium.urls')),
]

