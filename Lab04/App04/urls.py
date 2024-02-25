from django.contrib import admin
from django.urls import path
from App04  import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # The default path for home
    path('<int:anyNumber>/', views.calculate_tax, name='calculate_tax'),  # The path for calculating tax, expecting an integer
    path('taxrate/', views.show_tax_rate, name='show_tax_rate'),  # The path for showing the tax rate
]