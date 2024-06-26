from django.urls import path
from main.apps import MainConfig
from main.views import (CompanyListView, CompanyDetailView,
                        CompanyCreateView, CompanyUpdateView, IndexView,
                        OfficeListView, OfficeDetailView, OfficeCreateView,
                        OfficeUpdateView, contacts, CompanyDeleteView,
                        OfficeDeleteView, BookingCreateView, CarsListView, CarsDetailView,
                        CarsCreateView, CarsUpdateView, CarsDeleteView, User_requestCreateView, User_requestListView,
                        User_requestDetailView, User_requestDeleteView, User_requestUpdateView, info, send_feedback,
                        User_requestStatusUpdateView, BookingListView, BookingUpdateView, BookingStatusUpdateView)

app_name = MainConfig.name

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('company_list', CompanyListView.as_view(), name='labtest_list'),
    path('company/<int:pk>', CompanyDetailView.as_view(), name='labtest_detail'),
    path('company_create/', CompanyCreateView.as_view(), name='labtest_create'),
    path('company_update/<int:pk>', CompanyUpdateView.as_view(), name='labtest_update'),
    path('company_delete/<int:pk>', CompanyDeleteView.as_view(), name='labtest_delete'),

    path('office_list', OfficeListView.as_view(), name='office_list'),
    path('office/<int:pk>', OfficeDetailView.as_view(), name='office_detail'),
    path('office_create/', OfficeCreateView.as_view(), name='office_create'),
    path('office_update/<int:pk>', OfficeUpdateView.as_view(), name='office_update'),
    path('office_delete/<int:pk>', OfficeDeleteView.as_view(), name='office_delete'),

    path('booking_create/', BookingCreateView.as_view(), name='booking_create'),
    path('booking_list', BookingListView.as_view(), name='booking_list'),
    path('booking_update/<int:pk>', BookingUpdateView.as_view(), name='booking_update'),
    path('booking/update/<int:pk>/', BookingStatusUpdateView.as_view(), name='booking_status_update'),

    path('cars_list', CarsListView.as_view(), name='cars_list'),
    path('car/<int:pk>', CarsDetailView.as_view(), name='car_detail'),
    path('car_create/', CarsCreateView.as_view(), name='car_create'),
    path('car_update/<int:pk>', CarsUpdateView.as_view(), name='car_update'),
    path('car_delete/<int:pk>', CarsDeleteView.as_view(), name='car_delete'),

    path('request_create/', User_requestCreateView.as_view(), name='request_create'),
    path('request_list/', User_requestListView.as_view(), name='request_list'),
    path('request_update/<int:pk>', User_requestUpdateView.as_view(), name='request_update'),

    path('info/', info, name='info'),

    path('send_feedback/', send_feedback, name='send_feedback'),
    path('user-requests/update/<int:pk>/', User_requestStatusUpdateView.as_view(), name='request_status_update'),
    path('booking_create/', BookingCreateView.as_view(), name='booking_create')
]
