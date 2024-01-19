"""Module providingFunction printing python version."""
from django.urls import path
from . import views


urlpatterns =[
    path('', views.myfunctioncall, name="index"),
    path('about', views.myfuncabout, name="about"),
    path('add/<int:a>/<int:b>', views.add,name="add"),
    path('intro/str:name/<int:age>', views.intro, name="intro"),
    path('firapp', views.myfirapp,name='firapp'),
    path('mysecpage',views.mysecpage,name="secpage"),
    path('mythirpage',views.mythirpage,name="thirpage"),
    path('imgpage',views.myimgpage,name="imgpng"),
    path('imgpage3',views.myimgpage3,name="imgpng3"),
    path('imgpage2',views.myimgpage2,name="imgpng2"),
    path('imgpage4',views.myimgpage4,name='imgpng4'),
    path('imgpage5/<str:imagename>',views.myimgpage5,name='imgpng5'),
    path('myform',views.myform,name='myform'),
    path('submit',views.submit,name='submitf'),
    path('form2',views.forms2,name='form2')
]