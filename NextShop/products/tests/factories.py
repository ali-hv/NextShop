from ..models import Product
import factory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('sentence', nb_words=4)
    slug = factory.Sequence(lambda n: 'product-{}'.format(n))
    description = factory.Faker('paragraph', nb_sentences=3)
    price = factory.Faker('random_number', digits=2, fix_len=True)
    stock = factory.Faker('random_int', min=0, max=100)
