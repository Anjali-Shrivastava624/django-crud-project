from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    # Students CRUD
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_create, name="student_create"),
    path("students/edit/<int:pk>/", views.student_update, name="student_update"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),
]
