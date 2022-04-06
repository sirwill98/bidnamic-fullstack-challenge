from datetime import datetime
from django.test import TestCase
from bidding_app.forms import ApplicationDataForm_part1, ApplicationDataForm_part2

class TestBiddingPart1Form(TestCase):
    def test_under_18(self):
        test_data = {
            'title': 'Mr',
            'first_name': 'test',
            'last_name': 'test',
            'date_of_birth': datetime.today().date(),
        }
        form = ApplicationDataForm_part1(test_data)
        valid_form = form.is_valid()
        return self.assertFalse(valid_form, form.errors)
    
    def test_empty_part1_form(self):
        form = ApplicationDataForm_part1()
        validate_form = form.is_valid()
        return self.assertFalse(validate_form)

class TestBiddingPart2Form(TestCase):
    def test_invalid_part2_form(self):
        valid_part2_data = {
            'company_name':'test company',
            'address':'123 test street',
            'telephone':'+447707777772',
            'bidding_settings':'Invalid Option',
            'google_ads_account_id':'1234567890'
        }

        part2_form = ApplicationDataForm_part2(valid_part2_data)
        valid_part2_data = part2_form.is_valid()

        error_message = part2_form.errors

        return self.assertFalse(valid_part2_data, error_message)

    def test_valid_part2_form(self):
        valid_part2_data = {
            'company_name':'test company',
            'address':'123 test street',
            'telephone':'+447707777772',
            'bidding_settings':'High',
            'google_ads_account_id':'1234567890'
        }
        part2_form = ApplicationDataForm_part2(valid_part2_data)
        valid_part2_data = part2_form.is_valid()
        return self.assertTrue(valid_part2_data, part2_form.errors)