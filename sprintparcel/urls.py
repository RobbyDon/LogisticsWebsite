from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('track/', views.tracking_form, name='track'),
    path('track/results/', views.tracking_results, name='tracking_results'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/cargo-transportation/', views.cargo_transportation, name='cargo_transportation'),
    path('services/air-freight/', views.air_freight, name='air_freight'),
    path('services/ocean-freight/', views.ocean_freight, name='ocean_freight'),
    path('services/road-freight/', views.road_freight, name='road_freight'),
    path('dashboard/tracking/', views.tracking_dashboard, name='tracking_dashboard'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
