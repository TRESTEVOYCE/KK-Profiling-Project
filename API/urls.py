from django.urls import path
from API import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserList.as_view(), name='user-detail'),
    path('profiling-informations/', views.ProfilingInformationsList.as_view(), name='profiling-informations-list'),
    path('profiling-informations/<int:pk>/', views.ProfilingInformationsList.as_view(), name='profiling-informations-detail'),
    path('kk-addresses/', views.KKAddressList.as_view(), name='kk-address-list'),
    path('kk-addresses/<int:pk>/', views.KKAddressList.as_view(), name='kk-address-detail'),
    path('youth-statuses/', views.YouthStatusList.as_view(), name='youth-status-list'),
    path('youth-statuses/<int:pk>/', views.YouthStatusList.as_view(), name='youth-status-detail'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventList.as_view(), name='event-detail'),
]