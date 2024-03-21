from django.urls import path
from news.apps import NewsConfig
from news.views import NewsCreateView, NewsListView, NewsDetailView, NewsUpdateView, NewsDeleteView

app_name = NewsConfig.name

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='create'),
    path('', NewsListView.as_view(), name='list'),
    path('view/<slug>/', NewsDetailView.as_view(), name='view'),
    path('edit/<slug>/', NewsUpdateView.as_view(), name='edit'),
    path('delete/<slug>', NewsDeleteView.as_view(), name='delete')

]