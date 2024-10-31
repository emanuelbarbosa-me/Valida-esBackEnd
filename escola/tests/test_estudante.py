from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class EstudanteviewsTesteCase(APITestCase):

    def setUp(self):
        # Cria um usuário de teste
        self.user = User.objects.create_user(
            username='joao',
            password='123456'
        )
        self.token = Token.objects.create(user=self.user)
        self.example_url = reverse('example')  # URL da sua view protegida

    def test_login(self):
        # Testa o login e obtenção do token
        response = self.client.post(reverse('api-login'), {
            'username': 'joao',
            'password': '123456'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_get_request(self):
        # Testa o método GET
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.example_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'GET request successful')

    def test_post_request(self):
        # Testa o método POST
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.example_url, {'data': 'value'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'POST request successful')

    def test_put_request(self):
        # Testa o método PUT
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(self.example_url, {'data': 'new_value'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'PUT request successful')

    def test_delete_request(self):
        # Testa o método DELETE
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(self.example_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'DELETE request successful')

    def test_patch_request(self):
        # Testa o método PATCH
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.patch(self.example_url, {'data': 'updated_value'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'PATCH request successful')
