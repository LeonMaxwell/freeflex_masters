from rest_framework import serializers

from courses.models import Course, Subscribe, LinksMaterialCourse, DocumentMaterialCourse, TextDescriptionMaterialCourse, MaterialCourse


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'count_rated', 'created_at',)


class SubscribeCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('user', 'course',)


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentMaterialCourse
        fields = ('document',)


class TextSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextDescriptionMaterialCourse
        fields = ('text',)


class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinksMaterialCourse
        fields = ('link',)

