from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import FileExtensionValidator


class Project(models.Model):
    SUBJECTS = (
        ("EN", "Английский"),
        ("RUS", "Русский"),
        ("MATH", "Математика"),
        ("PHYS", "Физика"),
        ("SOC", "Обществознание"),
        ("BIO", "Биология"),
        ("LIT", "Литература"),
        ("HIST", "История"),
        ("INF", "Информатика"),
        ("GEO", "География"),
        ("CHEM", "Химия")
    )
    title = models.CharField(max_length=127)
    short_description = models.CharField(max_length=255)
    creators = models.CharField(max_length=255)
    description = models.TextField()
    curator = models.CharField(max_length=127, blank=True, null=True)
    subject = models.CharField(choices=SUBJECTS, max_length=20, blank=True, null=True)

    presentation = models.FileField(upload_to='projects/presentations', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pptx', 'ppt'])])

    def get_all_images(self):
        return ProjectImage.objects.filter(project=self)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.get_all_images()) <= 8:
            super(Project, self).save()
        else:
            raise Exception("You can't upload more than 8 images for one project")

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/images')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.project.creators

    class Meta:
        verbose_name='Project'
        verbose_name_plural = 'Projects'