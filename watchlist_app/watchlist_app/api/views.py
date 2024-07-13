from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchmate.models import Movie

from .serializers import MovieSerializer


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)
