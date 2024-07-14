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


# NOTE - Model serializers
class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"
