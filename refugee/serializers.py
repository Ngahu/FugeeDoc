from rest_framework import serializers


from .models import (
    Refugee,
    PatientSymptom,
    Location,
    Entry
)


class RefugeeRegisterSerializer(serializers.ModelSerializer):
    """
    Description: SERializer to be used during the registering of a refugee.\n
    """
    class Meta:
        model = Refugee
        fields = (
            'first_name',
            'last_name',
            'phone_number',

        )
        
        def create(self,validated_data):
            new_refugee = Refugee(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                phone_number = validated_data['phone_number']
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
            'last_name',
            'phone_number'
        ]







class CreatePatientSymptomSerializer(serializers.ModelSerializer):
    '''
    Description:Create a single patient symptom.\n
    '''
    class Meta:
        model = PatientSymptom
        fields = [
            'common',
            'description'
        ]

        def create(self,validated_data):
            new_patient = PatientSymptom(
                common = validated_data['common'],
                description = validated_data['description']
            )
            new_patient.save()
            return new_patient




class PatientSymptomListSerializer(serializers.ModelSerializer):
    '''
    Description:This is going to list down the patients symptoms
    '''
    class Meta:
        model = PatientSymptom
        field = [
            'common',
            'description'
        ]






class LocationAddSerializer(serializers.ModelSerializer):
    '''
    Description:Create a location .\n
    '''
    class Meta:
        model = Location
        fields = [
            'latitude',
            'longitude',
            'village',
            'neighborhood',
            'compound'
        ]
        
        def create(self,validated_data):
            new_location = Location(
                latitude = validated_data['latitude'],
                longitude = validated_data['longitude'],
                village = validated_data['village'],
                neighborhood = validated_data['neighborhood'],
                compound = validated_data['compound']
            )
            new_location.save()

            return new_location








class EntryCreateSerializer(serializers.ModelSerializer):
    '''
    Description:Create a patient entry.\n
    '''
    class Meta:
        model = Entry
        fields = [
            'creator',
            'refugee',
            'symptoms',
            'location'
        ]

        def create(self,validated_data):
            new_entry = Entry(
                creator = validated_data['creator'],
                refugee = validated_data['refugee'],
                symptoms = validated_data['symptoms'],
                location = validated_data['location'],
            )
            new_entry.save()

            return new_entry

