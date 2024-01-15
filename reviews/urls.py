from django.urls import path

from reviews.views import ReviewListCreateView, ReviewLRetrieveUpdateDestroyView

urlpatterns = [
    path("", ReviewListCreateView.as_view(), name="review-list-create"),
    path(
        "<int:pk>/",
        ReviewLRetrieveUpdateDestroyView.as_view(),
        name="review-detail-view",
    ),
]
