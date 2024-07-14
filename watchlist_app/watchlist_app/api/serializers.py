from rest_framework import serializers
from watchmate.models import StreamPlatform, WatchList

# class MovieSerializer(serializers.Serializer):
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField()
# description = serializers.CharField()
# active = serializers.BooleanField()

# def create(self, validated_data):
#     return Movie.objects.create(**validated_data)


# def update(
#     self, instance, validated_data
# ):  # instance=old_value, validated_date=new_value
#     instance.name = validated_data.get("name", instance.name)
#     instance.description = validated_data.get("description", instance.description)
#     instance.active = validated_data.get("active", instance.active)
#     instance.save()
#     return instance


# NOTE - ModelSerializer
class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # NOTE -  name come from related_name="watchlist" in model
    # show all watchlists in 1 platform category, 1 platform: many movies
    # watchlist = WatchListSerializer(many=True, read_only=True)

    # NOTE - get movie title only from __str__ function
    # watchlist = serializers.StringRelatedField(many=True)

    # NOTE - get pk from watchlist
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # NOTE - get links from watchlist
    # NOTE - view_name comes from urls with endpoint: list/<int:pk>
    watchlist = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="watchlist-details"
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"
