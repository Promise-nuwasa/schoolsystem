from django.conf.urls import url
from django.urls import path,include
# from rest_framework import routers
# from .views import StudentViewSet
# router=routers.DefaultRouter()
# router.register("student/",StudentViewSet)
# urlpatterns=[
#     path("",include(router.urls)),
    
# ]
from django.urls import include, path
from rest_framework import routers
from .views import StudentViewSet,TrainerViewSet,CoursesViewSet,EventViewSet
router = routers.DefaultRouter()
router.register("student/", StudentViewSet)
router.register("trainer/", TrainerViewSet)
router.register("courses/", CoursesViewSet)
router.register("cal/", EventViewSet)




urlpatterns = [
    path("", include(router.urls))
]