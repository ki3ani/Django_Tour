from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kimani/kimani.html',views.kimani, name='kimani'),
    path('pn/pn.html', views.pn, name='pn'),
    path('<str:name>', views.greet, name='greet')
    
]

