from visualization import models
from rest_framework import viewsets, generics
from api_data import serializers
from rest_framework.response import Response

# Create your views here.
"""
:param pagination[page]: page number
:param pagination[perpage]: data per page

:type email: int
:type password: int

:return: Person List
:rtype: dict
:rmethod: GET
"""
class GetPersonsListView(viewsets.ViewSet):

    def list(self, request):
        page_num = int(request.GET.get('pagination[page]'))
        per_page = int(request.GET.get('pagination[perpage]'))
        start_from = 1 * ((page_num - 1) * per_page)
        end_in = per_page * page_num
        total = models.Person.objects.all().count()
        queryset = models.Person.objects.all()[start_from:end_in]
        serializer = serializers.GetPersonsListSerializer(queryset, many=True)
        return Response({
            'meta': {
                'page': page_num,
                'pages': 1,
                'perpage': per_page,
                'total': total,
                'sort': "asc",
                'field': "email"
            },
            'data': serializer.data
        })


"""
:param ids: persons ids to compare

:type ids: list

:return: selected persons List
:rtype: list
:rmethod: GET
"""
class CompareSelectedObjects(generics.ListAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def get_queryset(self):
        all_id = self.kwargs['ids'].split(',')
        queryset = models.Person.objects.filter(id__in=all_id)
        return queryset
