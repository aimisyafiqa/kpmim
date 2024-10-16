from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("mentor/", views.mentor, name="mentor"),
    path("course/", views.course, name="course"),
    path('course/update_course/<str:code>', views.update_course, name='update_course'),
    path('course/update_course/save_update_course/<str:code>', views.save_update_course, name='save_update_course'),
    path('course/delete_course/<str:code>', views.delete_course, name='delete_course'),
    path('mentor/update_mentor/<str:mentorcode>', views.update_mentor, name='update_mentor'),
    path('mentor/update_mentor/save_update_mentor/<str:mentorcode>', views.save_update_mentor, name='save_update_mentor'),
    path('mentor/delete_mentor/<str:mentorcode>', views.delete_mentor, name='delete_mentor'),
    path('course/search_course/', views.search_course, name='search_course'),
]