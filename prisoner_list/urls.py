from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prisoner_id>', views.delete, name='delete-prisoner'),
    path('add-prisoner', views.add_prisoner, name='add-prisoner'),
    path('search-prisoner', views.search_prisoner, name='search-prisoner')
]
