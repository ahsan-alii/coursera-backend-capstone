from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('api/menu-items/', views.menuItems),
    path('api/categories/', views.categories),
    path('book/', views.book, name="book"),
    path('blog/', views.formView, name="blog"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    # path('bookings/', views.bookings, name="bookings"),
]