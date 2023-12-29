from django.urls import path
# from .views import tracker_list, tracker_details
from set_tracker import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("trackers/", views.TrackerList.as_view()),
    path("tracker/<int:pk>/", views.TrackerDetails.as_view()),
    path("users/", views.UserList.as_view()),
    path("user/<int:pk>/", views.UserDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)