from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
      path('home/', views.home, name='home'),  # Sign-up page
     path('login/', views.login_view, name='login'),  # Updated to login_view
    path('dashboard/', views.dashboard, name='dashboard'),
    path('depart/', views.depart, name='depart'),
    path('status/', views.status, name='status'),
    path('complaint-form/', views.complaint_form, name='complaint_form'),
    path('complaint_submit/', views.complaint_submit, name='complaint_submit'),
    path('track/', views.track, name='track'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('transport/', views.transport, name='transport'),
    path('health/', views.health, name='health'),
path('education/', views.education, name='education'),
path('water/', views.water, name='water'),
path('electricity/', views.electricity, name='electricity'),
path('agriculture/', views.agriculture, name='agriculture'),

    path("villager-login/", views.villager_login, name="villager_login"),
    path("admin-login/", views.admin_login, name="admin_login"),
    #admin panel

       path('admin_dashboard', views.complaint_submit, name='admin_dashboard'),  # Add this line
       path('admin_dashboard', views.complaint_dashboard, name='admin_dashboard'),

       path('complaint_page', views.complaint_page, name='complaint_page'),

    path('select_role/', views.role_selection, name='role_selection'),  # Role selection page
     path('admin_login/', views.admin_login_view, name='admin_login'),
    # Add other URL patterns as needed
      

     path('complaint_details/<str:complaint_id>/', views.complaint_details, name='complaint_details'),

     path('complaint/update/<str:complaint_id>/', views.update_complaint_status, name='update_complaint_status'),

     path('status/', views.status, name='status'),

       path('complaint-counts/', views.complaint_counts, name='complaint_counts'),

      path('update-bulk-complaint-status/', views.update_bulk_complaint_status, name='update_bulk_complaint_status'),
]