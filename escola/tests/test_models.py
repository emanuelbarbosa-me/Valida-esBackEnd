from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante =Estudante.objects.create(
            nome = "teste do modelo estudante",
            email = 'test@gmail.com',
            cpf  = '15485412068',
            data_nascimento = '2023-03-23',
            celular = '86 99999-9999'
        )
    def test_verifica_atributos_de_estudantes(self):
        ''' testa os atributos de um estudante quando ele criado BD'''
        self.assertEqual(self.estudante.nome, 'teste do modelo estudante')
        self.assertEqual(self.estudante.email, 'test@gmail.com')
        self.assertEqual(self.estudante.cpf, '15485412068')
        self.assertEqual(self.estudante.data_nascimento, '2023-03-23')        
        self.assertEqual(self.estudante.celular, '86 99999-9999')
