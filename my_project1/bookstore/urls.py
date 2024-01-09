from django.urls import path
from . import views

urlpatterns=[
    path('store/',views.store),
    path('checkout/',views.checkout),
    path('main/',views.main),
    path('signup/',views.signup),
    path('login/',views.log_in),
    path('check/',views.check),
    path('cart/', views.view_cart)
    

]