from django.http import JsonResponse

from genres.models import Genre


# Create your views here.
def genre_view(request):
    genres = Genre.objects.all()
    return JsonResponse(
        [{"id": genre.id, "name": genre.name} for genre in genres], safe=False
    )
