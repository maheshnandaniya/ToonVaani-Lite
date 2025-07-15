from django.urls import path
from .views import cartoon_view

urlpatterns = [
    path('', cartoon_view, name='cartoon_home'),
]
