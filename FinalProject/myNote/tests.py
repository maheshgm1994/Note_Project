from django.test import TestCase
from .models import Notes
# Create your tests here.

class TestNotes(TestCase):
    # This is called before every test
    def setUp(self):
        # print("Calling setUp()")
        Notes.objects.create(name='Movie',text="My movie information")

    def test_Notes_add(self):
        c = Notes.objects.get(name='Movie')
        self.assertEqual(c.name, 'Movie')

    def test_Notes_count(self):
        c = Notes.objects.get(name='Education')
        self.assertEqual(c.expenditure_set.all().count(), 0)

    def test_Notes_delete(self):
        c = Notes.objects.get(name='Education')
        c.delete()
        self.assertRaises(Notes.DoesNotExist, Notes.objects.get, name='Education')

