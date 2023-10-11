import json

from django.core.serializers import serialize
from django.http import JsonResponse

from genres.models import Genre


# Create your views here.
def genre_list(request):
    genres = Genre.objects.all()
    serialized_data = serialize("json", genres)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False)
