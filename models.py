from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(null=False, unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.roll_no)

    class Meta:
        verbose_name = "student"
        managed = False
        db_table = 'student'

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    total_marks = models.IntegerField()
    percentage = models.IntegerField()

    # def __str__(self):
    #     return str(self.student.roll_no)

    class Meta:
        verbose_name = "Student Marks"
        managed = False
        db_table = 'marks'
