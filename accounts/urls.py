import imp
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import AddPostView, HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [  
    path('', views.indexView,name="home"),
    path('login_user', views.login_user,name="login_user"),
    path('dashboard/', views.dashboardView,name="dashboard"),
    path('post_page/', HomeView.as_view(), name="post_page"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('profile_page/', views.profileView,name="profile_page"),
    path('logout_user/',views.logout_user, name="logout_user"),
    path('register_user/',views.register_user, name="register_user"),
]