from django.urls import path

from .views import ActorListCreateView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path("", ActorListCreateView.as_view(), name="actor-list-create"),
    path(
        "<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail-view",
    ),
]
