from judicial.models import Process, PartiesInvolved, PartiesInvolvedProcess
from rest_framework import serializers


class PartiesInvolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartiesInvolved
        fields = '__all__'

class PartiesInvolvedProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartiesInvolvedProcess
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    parties_involved = PartiesInvolvedSerializer(many=True)

    class Meta:
        model = Process
        fields = '__all__'