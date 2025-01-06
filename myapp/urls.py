from django.urls import path
from . import views
from .views import payment_process
urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('login',views.user_login,name="login"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('download_ticket/<int:booking_id>/', views.download_ticket, name='download_ticket'),
    path('signout', views.signout, name="signout"),
    path('bookings/payement/<int:booking_id>/', views.payment_page, name='payement'),
    path('bookings/payement/success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('bookings/payement/success/<int:booking_id>/feedback/', views.FeedbackForm, name='feedback'),  # URL for feedback form
    path('bookings/payement/success/<int:booking_id>/feedback/list/', views.FeedbackList, name='feedback_list'),

]
