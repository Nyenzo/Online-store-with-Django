from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Cologne', slug='cologne')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Category object (1)')

class TestCategoriesModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Cologne', slug='cologne')
        User.objects.create(username='Admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price='7.00', image='django')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product)) 
        self.assertEqual(str(data), 'django beginners')
