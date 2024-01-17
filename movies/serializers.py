from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie


# # Este serializer abaixo não pode ser utilizado em métodos POST para criar instâncias
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
#     resume = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    # Declara um campo calculado
    rate = serializers.SerializerMethodField(read_only=True)

    # O campo calculado começa com get_[nome do campo a ser retornado pelo model]

    # def get_rate(movie):
    #     reviews = movie.reviews.all()
    #     if len(reviews) == 0:
    #         return None
    #     movie_ratings = []
    #     for review in reviews:
    #         movie_ratings.append(review.stars)
    #     if sum(movie_ratings) == 0:
    #         return 0
    #         # or return sum(movie_ratings) / len(movie_ratings)
    #     return round(mean(movie_ratings), 1)

    @staticmethod
    def get_rate(movie):
        rate = movie.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return None

    class Meta:
        model = Movie
        fields = "__all__"

    # VALIDAÇÕES
    # Toda validação começa com validate_[nome do campo a ser validado]
    @staticmethod
    def validate_release_date(value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990"
            )
        return value

    @staticmethod
    def validate_resume(value):
        if len(value) > 500:
            raise serializers.ValidationError(
                "O resumo do filme não pode ter mais do que 200 caracteres"
            )
        return value
