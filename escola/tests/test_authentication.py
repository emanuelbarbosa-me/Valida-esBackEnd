from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')        

    def test_autenticacao_user_com_credencias_Corretas(self):
        '''Teste que verifica se o login está acontecendo de forma correta'''
        usuario = authenticate(username='admin', password = 'admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_user_com_username_incorrento(self):
        '''Teste que verifica se se o login vai acusar erro quando o username está errado'''
        usuario = authenticate(username = 'admn', password = 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_com_password_incorrento(self):
        '''Teste que verifica se se o login vai acusar erro quando o username está errado'''
        usuario = authenticate(username = 'admn', password = 'admn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)