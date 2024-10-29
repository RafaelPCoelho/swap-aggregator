from django.test import TestCase
from profissional.models import Profissional

class ProfissionalModelTest(TestCase):
    def test_str_method(self):
        profissional = Profissional(nome="Lucas Silva", profissao="Programador")
        self.assertEqual(str(profissional), "Lucas Silva")
