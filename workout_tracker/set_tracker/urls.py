from django.urls import path
from .views import tracker_list, tracker_details
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("trackers/", tracker_list),
    path("tracker/<int:pk>/", tracker_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)