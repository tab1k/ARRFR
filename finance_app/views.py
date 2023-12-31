from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from finance_app.models import FinancialOrganization, Executive
from users.forms import UserPositionFilterForm
from users.models import UserPosition
from rest_framework import generics
from .models import Executive
from .serializers import ExecutiveSerializer


class IndexView(LoginRequiredMixin, ListView):
    model = FinancialOrganization
    template_name = 'finance_app/index.html'
    context_object_name = 'organizations'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['executive'] = Executive.objects.all()
        for organization in context['organizations']:
            executives_count = organization.executive_set.count()
            organization.bar_width = executives_count * 10
        return context


class ExecutiveListView(LoginRequiredMixin, ListView):
    model = Executive
    template_name = 'finance_app/executive_list.html'
    context_object_name = 'executive'

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        queryset = Executive.objects.filter(financial_organization_id=organization_id).order_by('-start_date')
        position_id = self.request.GET.get('position')
        if position_id:
            queryset = queryset.filter(position_id=position_id)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position'] = UserPosition.objects.all()
        context['organization'] = FinancialOrganization.objects.all()
        context['organization_id'] = self.kwargs['organization_id']
        context['filter_form'] = UserPositionFilterForm(self.request.GET)

        return context


# DRF

class ExecutiveListCreateView(generics.ListCreateAPIView):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer


class ExecutiveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer
