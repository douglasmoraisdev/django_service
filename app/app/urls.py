from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('django_service/polls/', include('polls.urls')),
    path('django_service/admin/', admin.site.urls),
]