from django.urls import path
from announcements.apps import AnnouncementsConfig
from announcements.views import (AnnouncementsListView, AnnouncementsDetailView,
                                 AnnouncementsUpdateView, AnnouncementsDeleteView, AnnouncementsCreateView)

app_name = AnnouncementsConfig.name

urlpatterns = [
    path('', AnnouncementsListView.as_view(), name='list'),
    path('create/', AnnouncementsCreateView.as_view(), name='create'),
    path('view/<slug>/', AnnouncementsDetailView.as_view(), name='view'),
    path('edit/<slug>/', AnnouncementsUpdateView.as_view(), name='edit'),
    path('delete/<slug>', AnnouncementsDeleteView.as_view(), name='delete')

]