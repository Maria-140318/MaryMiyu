from django.contrib import admin
from django.urls import path #, include, re_path
#from django.urls import re_path as url 
#from django.conf.urls import url
####Libraries for url
#from django.conf.urls import url
from django.urls import re_path 
#, handler404, handler500
from MSWE.views import EmpresaCreate, EmpresaList, EmpresaUpdate, EmpresaDelete ,Empresa
#from . import views
#url module
app_name="MSWE"
"""urlpatterns = [
    path('', views.EmpresaList, name='Empresalist'),
    #path('empresa/<int:pk>/', views.EmpresaDetail, name='Empresadetail'),
    path('empresa/new/', views.EmpresaCreate, name='add_empresa'),
    path('empresa/<int:pk>/edit/', views.EmpresaUpdate, name='modi_empresa'),
    path('empresa/<int:pk>/delete/', views.EmpresaDelete, name='eli_empresa'),
]
"""
urlpatterns = [
    #path('',Empresa),
    path('new/',EmpresaCreate.as_view(), name='add_empresa'),
    path('',EmpresaList.as_view(),name='ver_empresa'),
    path('empresa/modi/<int:EmpresaId>', EmpresaUpdate.as_view(), name='modi_empresa'),
    path('empresa/eli/<int:EmpresaId>', EmpresaDelete.as_view(), name='eli_empresa'),
    #url(r'^modificar_empresa/(?P<pk>\d+)/$', EmpresaUpdate.as_view(), name='modi_empresa'),
    #path('<int:pk>/delete/', EmpresaDelete.as_view, name='eli_empresa'),
    #re_path(r'^modificar_empresa/(?P<pk>\d+)/$',EmpresaUpdate.as_view(), name='modi_empresa'),
    #url('eliminar_empresa',EmpresaDelete.as_view(), name='eli_empresa')
]
