from rest_framework import serializers
from finance_app.models import Executive


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'