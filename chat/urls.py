from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('chat_home/', views.chat_home, name='chat_home'),
    path('chat/<int:sender>/<int:receiver>', views.chat_view, name='set_chat'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
]