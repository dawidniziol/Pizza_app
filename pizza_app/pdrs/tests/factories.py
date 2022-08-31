from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
import factory

class SuperUserFactory(DjangoModelFactory):
    """
    Factory for Superuser
    """
    class Meta:
        model = User

    username = 'admin'
    email = 'abc@abc.abc'
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_superuser = True
    is_active = True


class UserFactory(DjangoModelFactory):
    """
    Factory for User
    """
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'User' + str(n))
    email = 'abc@abc.abc'
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_superuser = False
    is_active = True
