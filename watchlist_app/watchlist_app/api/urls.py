from django.urls import path

from watchlist_app.api.views import (
    ReviewDetail,
    ReviewList,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    WatchDetailAV,
    WatchListAV,
)

urlpatterns = [
    path("platform/", StreamPlatformAV.as_view(), name="stream-platforms"),
    path(
        "platform/<int:pk>/", StreamPlatformDetailAV.as_view(), name="platform-details"
    ),
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("list/<int:pk>/", WatchDetailAV.as_view(), name="watchlist-details"),
    path(
        "platform/<int:pk>/review/",
        StreamPlatformDetailAV.as_view(),
        name="platform-details",
    ),
    path("platform/review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
