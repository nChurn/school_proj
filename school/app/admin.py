from django.contrib import admin
from .models import Project, ProjectImage

# Register your models here.
class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

# class PartnerImageAdmin(admin.StackedInline):
#     model = PartnerImage

# @admin.register(Partner)
# class PartnerAdmin(admin.ModelAdmin):
#     inlines = [PartnerImageAdmin]