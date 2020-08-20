
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('view/',views.UserView, name='view'),
   path('transaction/', views.trans, name='trans'),
   path('tr/',views.trview, name='tr')
]