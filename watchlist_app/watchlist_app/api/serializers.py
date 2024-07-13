from rest_framework import serializers
from watchmate.models import Movie


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")
    else:
        return value


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[name_length])
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(
        self, instance, validated_data
    ):  # instance=old_value, validated_date=new_value
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

    def validate(self, data):
        title = data.get("name")
        description = data.get("description")

        if title and description and title == description:
            raise serializers.ValidationError(
                "Title and Description should be different"
            )

        return data
