from django.urls import path
from .views import courses_profile, delete_courses, edit_courses, register_courses,course_list
urlpatterns=[path(
    "register/",register_courses,name="register_courses"),
        path("list/",course_list,name="course_list"),
          path("edit/<int:id>/",edit_courses,name="edit_courses"),
             path("profile/<int:id>/",courses_profile,name="courses_profile"),
             path("delete/<int:id/",delete_courses,name="delete_courses")

]