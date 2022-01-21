from django.contrib import admin
from courses.models import Course, Subscribe, LinksMaterialCourse, DocumentMaterialCourse, TextDescriptionMaterialCourse

admin.site.register(Course)
admin.site.register(LinksMaterialCourse)
admin.site.register(DocumentMaterialCourse)
admin.site.register(TextDescriptionMaterialCourse)
admin.site.register(Subscribe)