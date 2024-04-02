import factory
import os

from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True

    name = factory.Faker('sentence', nb_words=4)
    slug = factory.Sequence(lambda n: 'product-{}'.format(n))
    description = factory.Faker('paragraph', nb_sentences=3)
    price = factory.Faker('random_number', digits=2, fix_len=True)
    stock = factory.Faker('random_int', min=0, max=100)
    image = factory.django.ImageField(filename='test_image.jpg')

    @factory.post_generation
    def cleanup_files(obj, create, extracted, **kwargs):
        """
        Post-generation hook to clean up generated image files after the test.
        """
        if not create:
            # No object was created, do nothing
            return

        if not obj.image:
            # No image was generated for this object, do nothing
            return

        # Delete the generated image file
        if os.path.isfile(obj.image.path):
            os.remove(obj.image.path)
