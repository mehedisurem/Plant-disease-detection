
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="AboutUs"),
    path('pdf/',views.pdf, name="pdf"),
    path ('sadia/',views.sadia, name="sadia"),
    path ('mehenaz/',views.mehenaz, name="mehenaz"),
    path ('surem/',views.surem, name="surem"),
]