from rest_framework import serializers
from .models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__' # Expone todos los campos
        read_only_fields = ('fecha_registro',) # Protege la fecha para que no sea modificada