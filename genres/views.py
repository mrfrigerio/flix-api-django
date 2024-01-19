from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Create your views here.
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == "GET":
#         genres = Genre.objects.all()
#         return JsonResponse(
#             [{"id": genre.id, "name": genre.name} for genre in genres], safe=False
#         )
#     elif request.method == "POST":
#         data = json.loads(request.body.decode("utf-8"))
#         new_genre = Genre(name=data["name"])
#         new_genre.save()
#         return JsonResponse({"id": new_genre.pk, "name": new_genre.name}, status=201)
#
#
# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     if request.method == "GET":
#         return JsonResponse({"id": genre.id, "name": genre.name})
#     elif request.method == "PUT":
#         data = json.loads(request.body.decode("utf-8"))
#         genre.name = data["name"]
#         genre.save()
#         return JsonResponse({"id": genre.pk, "name": genre.name})
#     elif request.method == "DELETE":
#         genre.delete()
#         return JsonResponse({"message": "deleted"}, status=204)
