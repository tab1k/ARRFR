from finance_app.views import *
from django.urls import path, include

app_name = 'finance_app'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('financial-organizations/<int:organization_id>/', ExecutiveListView.as_view(), name='executive'),
    #DRF
    path('api/executives/', ExecutiveListCreateView.as_view(), name='executive-list-create'),
    path('api/executives/<int:pk>/', ExecutiveDetailView.as_view(), name='executive-detail'),
]
