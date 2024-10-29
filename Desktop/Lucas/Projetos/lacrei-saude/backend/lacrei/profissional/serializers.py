from rest_framework import serializers
from profissional.models import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id', 'nome', 'profissao', 'endereco', 'contato']

    def validate_contato(self, value):
        cleaned_value = value.replace(" ", "")
        if not cleaned_value.isdigit():
            raise serializers.ValidationError("O contato deve conter somente números.")
        return value
