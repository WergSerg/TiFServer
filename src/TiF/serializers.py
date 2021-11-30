from rest_framework import serializers

from src.TiF.models import User,   Text, Comment, Choice, Mpaa, Foundation, TextDep, Hashtag, Category



class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()

    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'password2']

    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email=self.validated_data['email'],  # Назначаем Email
            username=self.validated_data['username'],  # Назначаем Логин
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        password2 = self.validated_data['password2']
        # Проверяем совпадают ли пароли
        if password != password2:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя
        return user

class FoundationSerialize(serializers.ModelSerializer):
    class Meta:
        model = Foundation
        fields = ['id','name']


class TextDepNestedSerializer(serializers.ModelSerializer):
    found = FoundationSerialize()

    class Meta:
        model = TextDep
        fields = ['found']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['tag_name']


class UserSerializerName(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["name"]


class MpaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpaa
        fields = ["name", "description"]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializerName()

    class Meta:
        model = Comment
        fields = ["timestamp", "author", "text"]


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


class FoundationReverseSerialize(serializers.ModelSerializer):
    text_deps = serializers.SerializerMethodField(source='count_text')

    class Meta:
        model = Foundation
        fields = ['id','name', 'text_deps']

    def get_text_deps(self, obj):
        return obj.text_deps.count()



class CategoryReverseSerialize(serializers.ModelSerializer):
    categorys = FoundationReverseSerialize(many=True)

    class Meta:
        model = Category
        fields = ['name', 'categorys']


class CreateTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class CategorySerialize(serializers.ModelSerializer):
    categorys = FoundationSerialize(many=True)

    class Meta:
        model = Category
        fields = ['id','name', 'categorys']

