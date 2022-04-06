from django.test import TestCase
from bidding_app.models import ClientApplicationData
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

class ViewAllRecords(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='test12345')
        self.client = Client()

        i = 0
        while i < 3:
            ClientApplicationData.objects.create(
                user = User.objects.get(username='test'),
                title='Mr',
                first_name='test',
                last_name='test',
                date_of_birth=date(1998,10,24),
                company_name='test company',
                address='123 test street',
                telephone='+447707777772',
                bidding_settings='High',
                google_ads_account_id='1234567890'
            )
            i+=1


    def test_view_applications(self):
        browser = self.client
        user = User.objects.get(username='test')
        browser.force_login(user)
        response = browser.get(reverse('view-bids'))
        # assert the right amount of records are displaying
        self.assertEqual(len(response.context['query_results']), 3)


    def test_delete_then_view_application(self):
        browser = self.client
        user = User.objects.get(username='test')
        browser.force_login(user)
        response = browser.get(reverse('delete-bid', kwargs={'id':1}))
        response = browser.get(reverse('view-bids'))
        # assert the right amount of records are displaying
        self.assertEqual(len(response.context['query_results']), 2)