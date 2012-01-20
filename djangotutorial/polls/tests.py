#-*- coding: utf-8 -*-
import datetime

from django.test import TestCase

from polls.models import Poll

class ModelsTest(TestCase):
    
    def test_poll_was_published_today(self):
        poll = Poll.objects.create(
            question='ShiningPanda is awesome no?',
            pub_date=datetime.datetime.now(),
        )
        self.assertTrue(poll.was_published_today())
