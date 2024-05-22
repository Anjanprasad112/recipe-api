from django.test import TestCase
from users.models import CustomUser
from recipe.models import RecipeCategory, Recipe

class RecipeModelTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create(email='test@example.com', username='testuser')
        # Create a category
        self.category = RecipeCategory.objects.create(name='Test Category')

    def test_recipe_creation(self):
        """Test recipe creation"""
        recipe = Recipe.objects.create(
            author=self.user,
            category=self.category,
            title='Test Recipe',
            desc='Test description',
            cook_time='00:30:00',
            ingredients='Test ingredients',
            procedure='Test procedure'
        )
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.desc, 'Test description')
        self.assertEqual(recipe.category, self.category)
