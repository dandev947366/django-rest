from django.urls import include, path

# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import MovieDetailAV, MovieListAV

urlpatterns = [
    # path("list/", movie_list, name="movie-list"),
    # path("<int:pk>", movie_details, name="movie-detail"),
    path("list/", MovieListAV.as_view(), name="movie-list"),
    path("<int:pk>", MovieDetailAV.as_view(), name="movie-detail"),
]
