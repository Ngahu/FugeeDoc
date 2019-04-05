from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'phone_number',
            'first_name',
            'last_name',
            'password',
        )

    write_only_fields = ('password',)
    read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

