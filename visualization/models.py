from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from dateutil import relativedelta
# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(TimeStampMixin):

    CONTRACT_TYPE_CHOICES = (
        (1, 'Permanent'),
        (2, 'Temporary'),
    )

    EMPLOYMENT_TYPE_CHOICES = (
        (1, 'Full-Time'),
        (2, 'Part-Time'),
    )

    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Passive'),
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    POTENIAL_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )

    PERFORMANCE_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5'),
    )

    OVERTIME_CHOICES = (
        (1, 'Unknown'),
        (2, 'Yes'),
        (3, 'No'),
    )

    email = models.EmailField(_('email address'), max_length=30)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    position = models.CharField(_('job'), max_length=30)
    department = models.CharField(_('department name'), max_length=50)
    birth_date = models.DateField(_('employee age'))
    salary = models.IntegerField(_('employee salary'))
    contract_type = models.CharField(_('type of contract'), max_length=9, choices=CONTRACT_TYPE_CHOICES)
    status = models.CharField(_('employment status'), max_length=7, choices=STATUS_CHOICES)
    type = models.CharField(_('type of employment'), max_length=9, choices=EMPLOYMENT_TYPE_CHOICES)
    ethnicity = models.CharField(_('employee ethnicity'), max_length=32)
    gender = models.CharField(_('employee gender'), max_length=6, choices=GENDER_CHOICES)
    risk = models.IntegerField(_('risk of exit'))
    compa = models.IntegerField(_('compa ratio'))
    tenure = models.IntegerField(_('tenure'))
    start_date = models.DateField(_('employee started work'))
    hours = models.IntegerField(_('scheduled hours'))
    potenial = models.CharField(_('potenial'), max_length=16, choices=POTENIAL_CHOICES)
    performance = models.CharField(_('performance rating'), max_length=7, choices=PERFORMANCE_CHOICES)
    overtime = models.CharField(_('overtime'), max_length=16, choices=OVERTIME_CHOICES)

    def get_employee_age(self):
        today = datetime.date.today()
        return relativedelta.relativedelta(today, self.birth_date).years

    def get_employee_start_date(self):
        today = datetime.date.today()
        diff = relativedelta.relativedelta(today, self.start_date)
        return F"{diff.years} years {diff.months} months"

    def __str__(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    class Meta:
        ordering = ['pk']
