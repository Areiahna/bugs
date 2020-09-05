"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bug_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view,),
    path('addTicket/<int:ticket_id>/edit/', views.edit_ticket_view),
    path('addTicket/', views.addTicket_view, name="addTicket"),
    path('ticketDetail/<int:ticket_id>/',
         views.ticketDetail_view, name="ticketDetail"),
    path('userDetail/<int:user_id>/',
         views.userdetail_view, name="userDetail"),
    path('assignTicket/<int:ticket_id>/', views.assignticket_view),
    path('admin/', admin.site.urls),
]
