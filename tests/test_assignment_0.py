"""
Assignment 0: Environment Check Tests

Te testy sprawdzają czy środowisko Django jest poprawnie skonfigurowane
i czy wszystkie podstawowe komponenty działają.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings


class Assignment0EnvironmentCheckTestCase(TestCase):
    """Testy sprawdzające poprawność konfiguracji środowiska"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_page_accessible(self):
        """Test 1: Sprawdza czy strona główna jest dostępna"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django Workshop')
    
    def test_home_page_contains_success_message(self):
        """Test 2: Sprawdza czy strona zawiera komunikat o sukcesie"""
        response = self.client.get('/')
        self.assertContains(response, 'SUCCESS')
        self.assertContains(response, 'środowisko Django jest poprawnie skonfigurowane')
    
    def test_health_check_endpoint(self):
        """Test 3: Sprawdza czy endpoint health check działa"""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'OK')
    
    def test_admin_panel_accessible(self):
        """Test 4: Sprawdza czy panel administracyjny jest dostępny"""
        response = self.client.get('/admin/')
        # Powinien przekierować do logowania (302) lub pokazać stronę logowania (200)
        self.assertIn(response.status_code, [200, 302])
    
    def test_static_files_configured(self):
        """Test 5: Sprawdza czy static files są poprawnie skonfigurowane"""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertEqual(settings.STATIC_URL, '/static/')
        self.assertTrue(hasattr(settings, 'STATICFILES_DIRS'))
    
    def test_templates_configured(self):
        """Test 6: Sprawdza czy templates są poprawnie skonfigurowane"""
        template_dirs = settings.TEMPLATES[0]['DIRS']
        self.assertTrue(len(template_dirs) > 0)
        self.assertTrue(str(template_dirs[0]).endswith('templates'))
    
    def test_database_configuration(self):
        """Test 7: Sprawdza podstawową konfigurację bazy danych"""
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertIn('default', settings.DATABASES)
        # Sprawdza czy używa SQLite (domyślnie dla warsztatów)
        self.assertEqual(
            settings.DATABASES['default']['ENGINE'], 
            'django.db.backends.sqlite3'
        )
    
    def test_home_url_name_works(self):
        """Test 8: Sprawdza czy URL name 'home' działa poprawnie"""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_health_check_url_name_works(self):
        """Test 9: Sprawdza czy URL name 'health_check' działa poprawnie"""
        url = reverse('health_check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


@pytest.mark.django_db
class Assignment0PytestIntegrationTests:
    """Dodatkowe testy integracyjne używające pytest"""
    
    def test_django_settings_module_set(self):
        """Test 10: Sprawdza czy DJANGO_SETTINGS_MODULE jest ustawione"""
        import os
        django_settings = os.environ.get('DJANGO_SETTINGS_MODULE')
        assert django_settings is not None
        assert 'workshop_project.settings' in django_settings
    
    def test_secret_key_configured(self):
        """Test 11: Sprawdza czy SECRET_KEY jest skonfigurowany"""
        assert hasattr(settings, 'SECRET_KEY')
        assert len(settings.SECRET_KEY) > 10
        assert settings.SECRET_KEY != ''
    
    def test_debug_mode_enabled(self):
        """Test 12: Sprawdza czy DEBUG mode jest włączony (dla development)"""
        assert settings.DEBUG is True
    
    def test_allowed_hosts_configured(self):
        """Test 13: Sprawdza czy ALLOWED_HOSTS są skonfigurowane dla Codespaces"""
        assert hasattr(settings, 'ALLOWED_HOSTS')
        # Powinna być skonfigurowana dla Codespaces
        assert '*' in settings.ALLOWED_HOSTS or len(settings.ALLOWED_HOSTS) > 0