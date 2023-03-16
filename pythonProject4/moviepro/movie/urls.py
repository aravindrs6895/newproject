from django.urls import path
from . import views

app_name='movie'

urlpatterns=[
    path('',views.note,name='fed'),
    path('movie/<int:id>/', views.detail, name='detail'),
    path('z',views.happy,name='dope'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('as',views.movielistview.as_view(),name='as'),
    path('ad/<int:pk>/',views.moviedetailview.as_view(),name="ad"),
    path("cbvupdate/<int:pk>/",views.movieupdateview.as_view(),name="cbvupdate"),
    path("cbvdelete/<int:pk>/",views.moviedeleteview.as_view(),name="cbvdelete")
]