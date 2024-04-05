from django.contrib.auth import get_user_model
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        skip_postgeneration_save = True

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    name = factory.Faker('name')

    # Set password for created user
    _password_value = factory.faker.faker.Faker().password()
    password = factory.PostGenerationMethodCall('set_password', _password_value)
