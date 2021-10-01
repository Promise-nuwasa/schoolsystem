from django.test import TestCase
import datetime
from.models import Trainer
from django.urls import reverse

# Create your tests here.
class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(
            first_name="James",
            last_name="Mwai",
            age=34
)

# Create your tests here.


def test_full_name_contain_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
   
def test_full_name_contain_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())

# def test_year_of_birth(self):
#         year=datetime.datetime.now().year-self.trainer.age
#         # year=2021-self.student.age 
#         self.assertEqual(year,self.trainer.year_of_birth())  

def test_trainer_registration_view(self):
        self.data={"first_name":self.trainer.first_name,
                "last_name":self.trainer.last_name,
                "age":self.trainer.age
        }
        url=reverse("register_trainer")
        response=self.client.post(url,self.data)
        self.assertEqual(response.status_code,200)