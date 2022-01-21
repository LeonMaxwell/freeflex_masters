from django.urls import path

from courses.views import CourseListAPIView, SubscribeCourseAPIVIew, LikesCourseAPIVIew, MaterialsAPIVIew

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='list_courses'),
    path('<int:pk>/subscribe/', SubscribeCourseAPIVIew.as_view(), name='subscribe_course'),
    path('<int:pk>/materials/', MaterialsAPIVIew.as_view(), name='materials_course'),
    path('<int:pk>/like/', LikesCourseAPIVIew.as_view(), name='rated_course')
]