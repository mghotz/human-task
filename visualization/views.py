from django.shortcuts import render
from django.views import View
import io, csv
from visualization import models
from django.http import JsonResponse
from django.contrib.auth import views
import requests
# Create your views here.

# upload persons from CSV file
class PersonsUploadView(View):

    def get(self, request):
        template_name = 'importpersons.html'
        return render(request, template_name)

    def post(self, request):
        personsFile = io.TextIOWrapper(request.FILES['persons'].file)
        persons = csv.DictReader(personsFile)
        list_of_dict = list(persons)
        objs = [
            models.Person(
                email=list_of_dict[i]['Email Id'],
                first_name=list_of_dict[i]['First name'],
                last_name=list_of_dict[i]['Last name'],
                position=list_of_dict[i]['Position'],
                department=list_of_dict[i]['Department'],
                birth_date=list_of_dict[i]['Birth Date'],
                salary=list_of_dict[i]['Salary'].split('$')[0],
                contract_type=list_of_dict[i]['Contract type'],
                status=list_of_dict[i]['Employment status'],
                type=list_of_dict[i]['Employment type'],
                ethnicity=list_of_dict[i]['Ethnicity'],
                gender=list_of_dict[i]['Gender'],
                risk=list_of_dict[i]['Risk of exit'].split('%')[0],
                compa=list_of_dict[i]['Compa Ratio'].split('%')[0],
                tenure=list_of_dict[i]['Tenure'].split(' ')[0],
                start_date=list_of_dict[i]['Start date'],
                hours=list_of_dict[i]['Scheduled Hours'].split(' ')[0],
                potenial=list_of_dict[i]['Potenial'],
                performance=list_of_dict[i]['Performance rating'],
                overtime=list_of_dict[i]['Overtime status']
            )
            for i in range(len(list_of_dict))
        ]

        try:
            models.Person.objects.all().delete()
        except:
            pass

        try:
            msg = models.Person.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}

        except Exception as e:
            #print('Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}

        return JsonResponse(returnmsg)

class PersonDataTableView(views.TemplateView):
    template_name = 'data/table.html'

class ComparePersonDataView(views.TemplateView):
    template_name = 'data/compare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = F"http://localhost:8000/api/compare/{self.kwargs['ids']}/"
        data = requests.get(url=url)
        context['total'] = len(data.json())
        context['data'] = data.json()
        return context