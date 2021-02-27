from django.urls import path
from visualization import views

urlpatterns = [
    path('upload/', views.PersonsUploadView.as_view(), name='upload_csv'),
    path('compare/<str:ids>/', views.ComparePersonDataView.as_view(), name='compare_persons'),
    path('', views.PersonDataTableView.as_view(), name='data_table'),
]