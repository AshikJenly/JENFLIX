from django.urls import path

from .views import home_page_view,Register_page_view,Otpview,logout

urlpatterns = [path("", home_page_view),
               path("Register/",Register_page_view),
               path("Register/otp",Otpview),
               path("logout/",logout),
               ]
