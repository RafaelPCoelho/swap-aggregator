from django.test import TestCase
from profissional.models import Profissional
from profissional.serializers import ProfissionalSerializer

# Serialization
class TestProfissionalSerializer(TestCase):
    def test_serialization(self):
        
        profissional = Profissional(
            nome="Lucas Silva", 
            profissao="Programador", 
            endereco="Rua Futuro, 2", 
            contato="81 99991 9999"
        )

        serializer = ProfissionalSerializer(profissional)

        expected_data = {
            'id': None,  # Mock
            'nome': 'Lucas Silva',
            'profissao': 'Programador',
            'endereco': 'Rua Futuro, 2',
            'contato': '81 99991 9999'
        }
        
        self.assertEqual(serializer.data, expected_data)


# Deserialization
class TestProfissionalDeserializer(TestCase):
    def test_valid_deserialization(self):
        json_data = {
            'nome': 'João Medeiros',
            'profissao': 'Designer',
            'endereco': 'Avenida Brasil, 100',
            'contato': '81 99992 8888'
        }

        serializer = ProfissionalSerializer(data=json_data)
        
        self.assertTrue(serializer.is_valid()) 

        profissional = serializer.save()
        self.assertEqual(profissional.nome, 'João Medeiros')