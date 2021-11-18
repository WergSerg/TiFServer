from rest_framework import serializers

from .models import User, Message, Text,Comment, Choice,Mpaa,Foundation,TextDep,Hashtag


class FoundationSerialize(serializers.ModelSerializer):
    class Meta:
        model = Foundation
        fields = ['name']

class TextDepNestedSerializer(serializers.ModelSerializer):
    found=FoundationSerialize()
    class Meta:
        model = TextDep
        fields = ['found']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['tag_name']

class UserSerializerName(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["username"]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["name"]

class MpaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpaa
        fields = ["name","description"]

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializerName()
    class Meta:
        model = Comment
        fields = ["timestamp", "author","text"]

class TextNestedSerilizer(serializers.ModelSerializer):
    tagname = TagSerializer(many=True)
    text_deps = TextDepNestedSerializer(many=True)
    owner = UserSerializerName()
    status = ChoiceSerializer()
    mpaa = MpaaSerializer()
    comment = CommentSerializer(many=True)

    class Meta:
        model = Text
        fields = "__all__"