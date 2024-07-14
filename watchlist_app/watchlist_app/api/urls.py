from django.urls import include, path

# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (
    ReviewDetail,
    ReviewList,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    WatchDetailAV,
    WatchListAV,
)

urlpatterns = [
    # path("list/", movie_list, name="movie-list"),
    # path("<int:pk>", movie_details, name="movie-detail"),
    path("platform/", StreamPlatformAV.as_view(), name="stream-platforms"),
    path(
        "platform/<int:pk>", StreamPlatformDetailAV.as_view(), name="platform-details"
    ),
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("list/<int:pk>", WatchDetailAV.as_view(), name="watchlist-details"),
    path("review", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
