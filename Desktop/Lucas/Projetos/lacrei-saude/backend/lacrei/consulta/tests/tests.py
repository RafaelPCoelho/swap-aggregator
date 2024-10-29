from django.test import TestCase
from consulta.models import Consulta
from profissional.models import Profissional
from datetime import date

class ConsultaModelTest(TestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome="Lucas Silva", 
            profissao="Programador", 
            endereco="Rua Futuro, 2", 
            contato="81 99991 9999"
        )

    def test_str_method(self):
        consulta = Consulta.objects.create(
            data=date(2024, 10, 30), 
            profissional=self.profissional
        )

        expected_str = "Consulta em 2024-10-30 com Lucas Silva"
        self.assertEqual(str(consulta), expected_str)
