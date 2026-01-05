from django.urls import path
from .views import recommend_plants

urlpatterns = [
    path("recommend-plants/", recommend_plants),
]


