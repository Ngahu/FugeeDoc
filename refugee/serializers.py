from rest_framework import serializers


from .models import Refugee


class RefugeeRegisterSerializer(serializers.ModelSerializer):
    """
    Description: SERializer to be used during the registering of a refugee.\n
    """
    class Meta:
        model = Refugee
        fields = (
            'first_name',
            'last_name'

        )
        
        def create(self,validated_data):
            new_refugee = Refugee(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
            )
            new_refugee.save()

            return new_refugee








class RefugeeListSerializer(serializers.ModelSerializer):
    """
    Description:List down all registered  refugees.\n
    """
    class Meta:
        model = Refugee
        fields = [
            'first_name',
            'last_name'
        ]