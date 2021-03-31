from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    url(r'^homolog/'), include([
        path(r'^django_service/polls/', include('polls.urls')),
        path(r'^django_service/admin/', admin.site.urls),
    ])
]
