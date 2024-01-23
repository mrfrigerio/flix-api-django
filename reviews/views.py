from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalPermissionClass
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewLRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
