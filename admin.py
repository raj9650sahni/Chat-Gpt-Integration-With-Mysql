
from django.contrib import admin
from chat_gpt_integration.models import Student, Marks


class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'first_name', 'last_name', 'address', 'city']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'physics', 'chemistry', 'maths', 'total_marks', 'percentage']


admin.site.register(Student, StudentAdmin)
admin.site.register(Marks, MarksAdmin)