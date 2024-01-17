from django.urls import path

from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("", GenreCreateListView.as_view(), name="genre-create-list"),
    path(
        "<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
