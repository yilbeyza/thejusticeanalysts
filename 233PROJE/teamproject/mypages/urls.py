from django.urls import path




#from .views import HomepageView
from .views import ContactUsView
from .views import AllDataView
from .views import index



urlpatterns=[
    path('', index, name='homepage'),
    path('posts/', ContactUsView.as_view(), name='ContactUs'),
    path('alldata/', AllDataView.as_view(), name='AllData'),

]