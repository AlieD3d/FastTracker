from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ValidationError
from api import conf

User = get_user_model()


class UserSerializer(ModelSerializer):
    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous or (user == obj):
            return False
        return user.subscribe.filter(id=obj).exists()

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            username=validate_data['username'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

    def validate_username(self, username):
        if len(username) > conf.MAX_LEN_USERS_CHAR:
            raise ValueError(
                'Длина username допустима от '
                f'{conf.MIN_LEN_USERS_CHAR} до {conf.MAX_LEN_USERS_CHAR}'
            )
        if not username.isalpha():
            raise ValidationError(
                'В поле username допустимы только буквы'
            )
        return username.capitalize()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = 'is_subscribed'
