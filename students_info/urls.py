from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('genneral', views.genneral, name="genneral"),
    path('special_subjects', views.special_subjects, name="special_subjects"),
    path('elective_subjects', views.elective_subjects, name="elective_subjects"),
    path('about', views.about, name="about"),


]

