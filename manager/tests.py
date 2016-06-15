# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import *
from blog.models import Message, Questionnaire


class TestViews(TestCase):

    SUCCESS_STATUS = 200

    def setUp(self):
        self.username = "ido"
        self.password = "idopass"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        enterprise = Enterprise(
            name = "I do",
            who = "Empresa de pedidos de namoro e casamento",
            phone_contact = "061987654321",
            email_contact = "ido@gmail.com",
            address = "Brasilia - DF"
        ).save()
        self.enterprise = Enterprise.objects.get(id=1)
        self.message = Message

    def test_index_page_request(self):

        url_to_test = reverse('home')
        response = self.client.get(url_to_test)
        
        self.assertEqual(self.SUCCESS_STATUS, response.status_code)
    
    def test_update_page_request(self):

        url_to_test = reverse('update_enterprise', kwargs={'enterprise_id': self.enterprise.id})
        response = self.client.login(username=self.username, password=self.password)
        response = self.client.get(url_to_test)
        self.assertEqual(self.SUCCESS_STATUS, response.status_code)

    def test_update_page_post(self):
        
        url_to_test = reverse('update_enterprise', kwargs={'enterprise_id': self.enterprise.id})
        self.client.login(username=self.username, password=self.password)
        attributes = {
            'name' : "I dont",
            'who' : self.enterprise.who,
            'phone_contact' : self.enterprise.phone_contact,
            'email_contact' : self.enterprise.email_contact,
            'address' : self.enterprise.address
        }
        response = self.client.post(url_to_test, attributes, follow=True)
        self.assertEqual(self.SUCCESS_STATUS, response.status_code)
        self.assertRedirects(response, reverse('index'))
