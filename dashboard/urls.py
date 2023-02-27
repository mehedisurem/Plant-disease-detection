
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="AboutUs"),
    path('pdf/', views.pdf, name="pdf"),
    path('sadia/', views.sadia, name="sadia"),
    path('mehenaz/', views.mehenaz, name="mehenaz"),
    path('surem/', views.surem, name="surem"),
    path('istiaq/', views.istiaq, name="istiaq"),
    path('rafi/', views.rafi, name="rafi"),
    path('jahedul/', views.jahedul, name="jahedul"),
    path('system/', views.system, name="system"),
    path('hardwere/', views.hardwere, name="hardwere"),
    path('merge/', views.merge, name="merge"),
    path('draft/', views.draft, name="draft"),
    path('survey_form/', views.survey_form, name="survey_form"),
    path('survey_ques/', views.survey_ques, name="survey_ques"),

]