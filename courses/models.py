import os
import uuid

from django.db import models

from profilecourses.models import ProfileUser


def get_file_path(instance, filename):
    # Функция для изменения названия файла на UUID4
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("material/", filename)


class Course(models.Model):
    """
    Класс курсов.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    count_rated = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = 'course'
        ordering = ('-created_at',)


class Subscribe(models.Model):
    """
    Класс хранящий информацию о подписке пользователя на курс

    """
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.user.username} подписался на курс {self.course.name}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        db_table = 'subscribe'


class MaterialCourse(models.Model):
    """
    Класс материалов курса
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        abstract = True


class LinksMaterialCourse(MaterialCourse):
    link = models.URLField(max_length=255, verbose_name="Ссылка")

    def __str__(self):
        return f"[Ссылка] к {self.course.name}"

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        db_table = "material_links"


class DocumentMaterialCourse(MaterialCourse):
    document = models.FileField(upload_to=get_file_path, blank=True, null=True, verbose_name="Документ")

    def __str__(self):
        return f"[Документ] к {self.course.name}"

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        db_table = "material_documents"


class TextDescriptionMaterialCourse(MaterialCourse):
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return f"[Текстовое описание] к {self.course.name}"

    class Meta:
        verbose_name = "Текстовое описание"
        verbose_name_plural = "Текстовое описание"
        db_table = "material_text"
