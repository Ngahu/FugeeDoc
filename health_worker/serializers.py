from rest_framework import serializers


from .models import HealthOfficer


class HealthOfficerRegisterSerializer(serializers.ModelSerializer):
    """
    Description: SERializer to be used during the registering of a health officer.\n
    """
    class Meta:
        model = HealthOfficer
        fields = (
            'user',

        )
        
        def create(self,validated_data):
            new_health_officer = HealthOfficer(
                user = validated_data['user'],
            )
            new_health_officer.save()

            return new_health_officer

