import uuid

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    is_complete = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'full_name', 'email', 'inn', 'provider_type',
                  'username', 'phone', 'is_complete')
        extra_kwargs = {
            'provider_type': {'write_only': True},
            'username': {'write_only': True, 'required': False}
        }

    def create(self, validated_data):
        # Generate and inject username and password because Django requires it
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(str(uuid.uuid4()))
        user.save()
        return user


class InnUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            'provider_type': {'write_only': True},
            'username': {'write_only': True, 'required': False},
            'inn': {'required': True}
        }

    def create(self, validated_data):
        validated_data['username'] = 'inn_{}'.format(validated_data['inn'])
        return super(InnUserSerializer, self).create(validated_data)


class ExternalIdUserSerializer(UserSerializer):
    external_id = serializers.CharField(write_only=True, required=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('external_id',)

    def create(self, validated_data):
        validated_data['username'] = 'eid_{}'.format(validated_data.pop('external_id'))
        return super(ExternalIdUserSerializer, self).create(validated_data)
