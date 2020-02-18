import django_filters
from polls.models import *
class LeaveFilter(django_filters.FilterSet):
    class Meta:
        model = Leave
        fields = '__all__'
        # exclude=['count']


class SalaryFilter(django_filters.FilterSet):
    class Meta:
        model = Salary
        fields = '__all__'
    

class PositionFilter(django_filters.FilterSet):
    class Meta:
        model = Position
        fields = '__all__'


class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = '__all__'