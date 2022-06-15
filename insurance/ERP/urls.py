from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.Dashboardv,name='dashboard'),
    path('admins/dashboard/',views.AdminDashboardv,name='admin_dashboard'),
    path('branch/information/',views.Branch_Infor_showV,name='branch_info_show'),
    path('branch/information/save/',views.Branch_Infor_saveV,name='branch_info_save'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
