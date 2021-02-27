from django.http import HttpResponse
from faker import Faker
import csv
import random

def datagenerate(records, headers, response):
    # using Faker for generating Fake person data
    fake = Faker('en_US')

    # creating csv file to write dictionary
    writer = csv.DictWriter(response, fieldnames=headers, delimiter=',', lineterminator='\n')
    writer.writeheader()

    # starting to generate data
    for i in range(records):
        full_name = fake.name()
        full_name_split = full_name.split(" ")
        first_name = full_name_split[0]
        last_name = full_name_split[1]
        domain_name = "@humanpanel.com"
        email = first_name + "." + last_name + domain_name

        start_date = fake.date_between(start_date='-30y', end_date='today')

        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)

        writer.writerow({
            "Email Id": email,
            "First name": first_name,
            "Last name": last_name,
            "Position": fake.job(),
            "Department": random.choice(['Administration', 'Marketing', 'Purchasing', 'Human Resources', 'Shipping', 'IT', 'Public Relations']),
            "Birth Date": birth_date,
            "Salary": F"{random.randint(20000, 200000)}$",
            "Contract type": random.choice(['Permanent', 'Temporary']),
            "Employment status": random.choice(['Active', 'Passive']),
            "Employment type": random.choice(['Full-Time', 'Part-Time']),
            "Ethnicity": random.choice(['Abazins', 'Abkhazians', 'Bemba', 'Berbers', 'Catalans', 'Choctaw', 'Chukchi', 'Dutch', 'English', 'Estonians', 'French', 'Germans', 'Greeks']),
            "Gender": random.choice(['Male', 'Female']),
            "Risk of exit": F"{random.randint(0, 100)}%",
            "Compa Ratio": F"{random.randint(0, 100)}%",
            "Tenure": F"{random.randint(1, 20)} months",
            "Start date": start_date,
            "Scheduled Hours": F"{random.randint(1, 8)} hours",
            "Potenial": random.choice(['Low', 'Medium', 'High']),
            "Permanent": random.choice(['Permanent', 'Temporary']),
            "Performance rating": random.choice(['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']),
            "Overtime status": random.choice(['Unknown', 'Yes', 'No']),
        })

    return response

def returnCSV(request):
    # generate object count
    records = 1000

    # data header
    headers = ["Email Id", "First name", "Last name", "Position", "Department", "Age", "Birth Date", "Salary",
               "Employment time", "Contract type", "Employment status", "Employment type", "Ethnicity", "Gender",
               "Risk of exit", "Compa Ratio", "Tenure", "Start date", "Scheduled Hours", "Potenial", "Permanent",
               "Performance rating", "Overtime status"]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # generate Fake data
    datagenerate(records, headers, response)

    return response