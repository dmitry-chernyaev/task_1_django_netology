from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'display_teachers')

    def display_teachers(self, obj):
        return ", ".join([teacher.name for teacher in obj.teachers.all()])
    display_teachers.short_description = 'Учителя'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')