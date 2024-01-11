from django.contrib import admin
from django.urls import path

import actors.views
import movies.views
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/", GenreCreateListView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
    path(
        "actors/", actors.views.ActorListCreateView.as_view(), name="actor-list-create"
    ),
    path(
        "actors/<int:pk>/",
        actors.views.ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail-view",
    ),
    path(
        "movies/", movies.views.MovieListCreateView.as_view(), name="movie-list-create"
    ),
    path(
        "movies/<int:pk>/",
        movies.views.MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-detail-view",
    ),
]
