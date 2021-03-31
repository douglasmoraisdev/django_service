from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    url(r'^homolog/'), include([
        path('django_service/polls/', include('polls.urls')),
        path('django_service/admin/', admin.site.urls),
    ])
]