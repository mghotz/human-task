from rest_framework import serializers
from visualization import models
import datetime
from dateutil import relativedelta

class GetPersonsListSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    employee_start_date = serializers.SerializerMethodField()

    def get_age(self, obj):
        today = datetime.date.today()
        return relativedelta.relativedelta(today, obj.birth_date).years

    def get_employee_start_date(self, obj):
        today = datetime.date.today()
        diff = relativedelta.relativedelta(today, obj.start_date)
        return F"{diff.years} years {diff.months} months"

    class Meta:
        model = models.Person
        fields = ['pk', 'first_name', 'last_name', 'position', 'department', 'age', 'salary', 'employee_start_date', 'birth_date']


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    employee_start_date = serializers.SerializerMethodField()

    def get_age(self, obj):
        today = datetime.date.today()
        return relativedelta.relativedelta(today, obj.birth_date).years

    def get_employee_start_date(self, obj):
        today = datetime.date.today()
        diff = relativedelta.relativedelta(today, obj.start_date)
        return F"{diff.years} years {diff.months} months"

    class Meta:
        model = models.Person
        fields = '__all__'