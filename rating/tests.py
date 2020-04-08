from django.test import TestCase

# Create your tests here.
import os
import importlib
import re
import inspect
import tempfile
import rating.models
from rating import forms
# from populate_rating import populate
from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}RTB TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"

class ProjectStructureTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.rango_app_dir = os.path.join(self.project_base_dir, 'rating')

    def test_project_created(self):
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'ratetehboba'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'ratetehboba', 'urls.py'))

        self.assertTrue(directory_exists,
                        f"{FAILURE_HEADER} RTB configuration directory does not exist.{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists,
                        f"{FAILURE_HEADER}project's urls.py module does not exist.{FAILURE_FOOTER}")

    def test_is_rating_app_configured(self):

        is_app_configured = 'rating' in settings.INSTALLED_APPS

        self.assertTrue(is_app_configured,
                        f"{FAILURE_HEADER}The rating app missing from  setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
    def test_is_users_app_configured(self):

        is_app_configured = 'users' in settings.INSTALLED_APPS

        self.assertTrue(is_app_configured,
                        f"{FAILURE_HEADER}users app missing from setting's INSTALLED_APPS list.{FAILURE_FOOTER}")


class ViewTests(TestCase):
    def setUp(self):
        self.views_module = importlib.import_module('rating.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('rating.urls')

    # Do some of the important views work/exist?
    def test_view_exists(self):
        name_exists = 'home' in self.views_module_listing
        is_callable = callable(self.views_module.home)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER} Home view missing {FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Check you have defined your home() view correctly. {FAILURE_FOOTER}")

def create_user_object():

    user = User.objects.get_or_create(username='testuser',
                                      first_name='Test',
                                      last_name='User',
                                      email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()

    return user

def create_super_user_object():
    """
    Helper function to create a super user (admin) account.
    """
    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')

def get_template(path_to_template):
    """
    Helper function to return the string representation of a template file.
    """
    f = open(path_to_template, 'r')
    template_str = ""

    for line in f:
        template_str = f"{template_str}{line}"

    f.close()
    return template_str


class AuthSetupTests(TestCase):

    def test_installed_apps(self):

        self.assertTrue('django.contrib.auth' in settings.INSTALLED_APPS)

    def test_model_admin_interface_inclusion(self):
        """
        Attempts to access the UserProfile admin interface instance.
        If we don't get a HTTP 200, then we assume that the model has not been registered. Fair assumption!
        """
        super_user = create_super_user_object()
        self.client.login(username='admin', password='testpassword')

        # The following URL should be available if the UserProfile model has been registered to the admin interface.
        response = self.client.get('/admin/rating/cafe/')
        self.assertEqual(response.status_code, 200,
                         f"{FAILURE_HEADER}didn't get a HTTP 200 status code.{FAILURE_FOOTER}")

