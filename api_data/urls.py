from django.urls import path
from api_data import views

urlpatterns = [
    path('persons_list/', views.GetPersonsListView.as_view({'get': 'list'}), name='list_of_persons'),
    path('compare/<str:ids>/', views.CompareSelectedObjects.as_view(), name='compare_persons'),
]