from accounts.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from .views import TuneListView
from .models import Tune

class TuneTests(TestCase): 
    @classmethod

    def setUpTestData(cls):
        cls.factory = RequestFactory()

        cls.user = CustomUser.objects.create_user(
            username="testuser", 
            email="test@email.com", 
            password="secret", 
            instrument="violin",
        )
        
        cls.tune = Tune.objects.create(
              title="A good title",
              composer="Bach",
              key="C Major",
              notes="Some notes",
              genre="Classical",
              performer=cls.user,
        )

    def test_get_absolute_url(self): 
        self.assertEqual(self.tune.get_absolute_url(), "/tunes/1/")

    def test_tune_content(self): 
        self.assertEqual(f"{self.tune.title}", "A good title") 
        self.assertEqual(f"{self.tune.composer}", "Bach") 
        self.assertEqual(f"{self.tune.key}", "C Major")
        self.assertEqual(f"{self.tune.notes}", "Some notes")
        self.assertEqual(f"{self.tune.genre}", "Classical")
        self.assertEqual(f"{self.tune.performer}", "testuser")

    def test_tune_list_view(self):
        request = self.factory.get('/tunes/')
        request.user = AnonymousUser()
        response = TuneListView.as_view()(request)
        self.assertEqual(response.status_code,302)
    
    def test_tune_list_view_with_valid_user(self):
        request = self.factory.get('/tunes/')
        request.user = self.user
        response = TuneListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'tunes/tune_list.html')

