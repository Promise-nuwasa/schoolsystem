from django.http import response
from django.test import TestCase
from django.urls import reverse
import datetime
# Create your tests here.
from.models import Student
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="James",
                             last_name="John",
                             age=20)
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    def test_year_of_birth(self):
        year=datetime.datetime.now().year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())
    def test_student_registration_view(self):
        self.data={
            "first_name":self.student.first_name,
            "last_name":self.student.last_name,
            "age":self.student.age
        }
        url=reverse("register_student")
        response=self.client.post(url,self.data)
        # self.assertEqual(response.status_code,200)