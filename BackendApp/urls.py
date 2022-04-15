from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',Signup.as_view(), name='authemail-signup'),
    path('login/', Login.as_view(), name='authemail-login'),
    path('update/<int:id>', Update.as_view(), name='authemail-Update'),

]