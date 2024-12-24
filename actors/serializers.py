from rest_framework import serializers
from actors.models import Actor


class ActorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"


class ActorNationalitiesSerializers(serializers.Serializer):

    @staticmethod
    def get_nationalities():
        return (
            ("FR", "Francês"),
            ("US", "Americano"),
            ("IT", "Italiano"),
            ("JP", "Japonês"),
            ("CH", "Chinês"),
            ("BR", "Brasileiro"),
            ("IN", "Indiano"),
            ("DE", "Alemão"),
            ("ES", "Espanhol"),
            ("GB", "Inglês"),
            ("MX", "Mexicano"),
            ("AU", "Australiano"),
            ("CA", "Canadense"),
            ("IS", "Israelense"),
        )
