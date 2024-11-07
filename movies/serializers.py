from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lancamento deve ser posterior a 1900")
        return value

    def validate_resume(self, value):
        if len(value) > 255:
            raise serializers.ValidationError(
                "O resumo deve ter no maximo 255 caracteres")
        return value

    def get_rate(self, object):
        rate = object.reviews.aggregate(Avg("stars")).get("stars__avg")
        if (rate):
            return round(rate)
        return None
