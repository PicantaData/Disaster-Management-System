from informational import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('info',views.info, name='info'),
    path('donate',views.donate,name='donate'),
    path('guideines',views.guidelines,name='guidelines')
]