
from django.contrib import admin
from django.urls import path, include
from . import views
from .API.model import get_recomend_and_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/', get_recomend_and_history),
    path('', include('frontend.urls')),
]
