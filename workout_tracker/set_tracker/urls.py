from django.urls import path
from .views import tracker_list, tracker_details

urlpatterns = [
    path("trackers/", tracker_list),
    path("tracker/<int:pk>/", tracker_details),
]