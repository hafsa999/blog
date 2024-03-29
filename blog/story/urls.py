from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post/<int:id>/',views.post,name='post'),
    path('create',views.create,name='create'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')
]