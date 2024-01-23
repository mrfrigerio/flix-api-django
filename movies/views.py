from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalPermissionClass
from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.
class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
