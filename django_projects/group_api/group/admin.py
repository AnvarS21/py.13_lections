from django.contrib import admin
from group.models import Teacher, Group, Student
# Register your models here.

admin.site.register(Teacher)
# admin.site.register(Group)
# admin.site.register(Student)

@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_full_name', 'contacts', 'groups_list')
    def student_full_name(self, obj):
        return obj

    def groups_list(self, obj):
        # print(obj.id, obj.first_name, obj.last_name, obj.contacts)
        # print(obj.groups.all(), '!!!')
        return [x for x in obj.groups.all()]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count', 'students_list')

    def students_list(self, obj):
        return [x for x in obj.students.all()]

    def count(self, obj):
        return obj.students.count()
