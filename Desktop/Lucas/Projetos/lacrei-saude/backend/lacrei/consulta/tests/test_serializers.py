from django.test import TestCase
from profissional.models import Profissional
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer
from datetime import date

# Serialization
class TestConsultaSerializer(TestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome="Lucas Silva",
            profissao="Programador",
            endereco="Rua Futuro, 2",
            contato="81999919999"
        )
    
    def test_serialization(self):
        consulta = Consulta(
            data=date(2024, 12, 21),
            profissional=self.profissional
        )
        
        serializer = ConsultaSerializer(consulta)
        
        expected_data = {
            'data': '2024-12-21',
            'profissional': self.profissional.id
        }
        
        self.assertEqual(serializer.data, expected_data)
        

# Deserialization
class TestConsultaDeserializer(TestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome= 'João Medeiros',
            profissao= 'Designer',
            endereco= 'Avenida Brasil, 100',
            contato= '81999928888'
        )
        
    def test_deserialization(self):
        json_data = {
            'data': '2024-12-21',
            'profissional': self.profissional.id
        }

        serializer = ConsultaSerializer(data=json_data)
        self.assertTrue(serializer.is_valid())
        
        consulta = serializer.save()        
        self.assertEqual(consulta.data, date(2024, 12, 21),)
        self.assertEqual(consulta.profissional.id, self.profissional.id)
        self.assertEqual(consulta.profissional.nome, 'João Medeiros')