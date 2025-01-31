from django.urls import path
from .views.home_view import home
from .views.drc_view import drc_view
from .views.neo_view import neo_view
from .views.dac_view import dac_view
from .views.dm_view import dm_view

urlpatterns = [
    path('', home, name='home'),
    path('drc/', drc_view, name='drc'),
    path('neo/', neo_view, name='neo'),
    path('dac/', dac_view, name='dac'),
    path('dm/', dm_view, name='dm'),
]
