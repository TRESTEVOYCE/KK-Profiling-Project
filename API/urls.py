from django.urls import path
from API import views

urlpatterns = [
    path('users/', views.UserList),
    path('profiling_informations/', views.ProfilingInformationsList,name='profiling_informations_list'),
    path('kk_addresses/', views.KKAddressList,name='kk_addresses_list'),
    path('youth_statuses/', views.YouthStatusList,name='youth_statuses_list'),
    path('events/', views.EventList,name='events_list'),
]