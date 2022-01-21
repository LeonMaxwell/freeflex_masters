from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Subscribe, DocumentMaterialCourse, LinksMaterialCourse, TextDescriptionMaterialCourse
from .serializers import CourseSerializers, DocumentSerializers, LinkSerializers, TextSerializers


class CourseListAPIView(APIView):
    """
    Представить список курсов
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        list_courses = Course.objects.all()
        serializer = CourseSerializers(list_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeCourseAPIVIew(APIView):
    """
    Представление оформляющее подписку на курс, только зарегистрированным пользователям.
    """

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        user = request.user
        try:
            sub = Subscribe.objects.get(course_id=pk, user_id=user.pk)
            return Response('Вы уже подписаны на этот курс', status=status.HTTP_208_ALREADY_REPORTED)
        except Subscribe.DoesNotExist:
            subscribe = Subscribe.objects.create(user=user, course=course)
            subscribe.save()
            return Response('Успешно подписались на курс', status=status.HTTP_200_OK)


class LikesCourseAPIVIew(APIView):
    """
    Представление позволяющее оценить курс зарегистрированному пользователю.
    """

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        user = request.user
        try:
            sub = Subscribe.objects.get(course_id=pk, user_id=user.pk)
            if user.rated:
                return Response("Вы уже оценили курс.", status=status.HTTP_208_ALREADY_REPORTED)
            else:
                course.count_rated += 1
                course.save()
                user.rated = True
                user.save()
                return Response("Вы успешно оценили курс.", status=status.HTTP_200_OK)
        except Subscribe.DoesNotExist:
            return Response("Вы не подписаны на курс.", status=status.HTTP_404_NOT_FOUND)


class MaterialsAPIVIew(APIView):

    def get_object(self, material, pk):
        try:
            return material.objects.filter(course_id=pk)
        except material.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = request.user
        documents = self.get_object(DocumentMaterialCourse, pk)
        links = self.get_object(LinksMaterialCourse, pk)
        texts = self.get_object(TextDescriptionMaterialCourse, pk)
        try:
            sub = Subscribe.objects.get(course_id=pk, user_id=user.pk)
            context = {
                'material':{
                    'documents': DocumentSerializers(documents, many=True).data,
                    'links': LinkSerializers(links, many=True).data,
                    'texts': TextSerializers(texts, many=True).data,
                }
            }
            return Response(context, status=status.HTTP_200_OK)
        except Subscribe.DoesNotExist:
            return Response("Вы не подписаны на курс.", status=status.HTTP_404_NOT_FOUND)
