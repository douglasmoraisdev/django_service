from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('homolog/django_service/polls/', include('polls.urls')),
    path('homolog/django_service/admin/', admin.site.urls),
]