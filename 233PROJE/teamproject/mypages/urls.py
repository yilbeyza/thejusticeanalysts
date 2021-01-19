from django.urls import path
#from .views import HomepageView
from .views import AllDataView
from .views import index
#from .views import BlogListView
from .views import comment
from .views import review
from .views import message




urlpatterns=[
    path('', index, name='homepage'),
    path('posts/', comment, name='posts'),
    path('posts/', review, name='posts'),
    path('alldata/', AllDataView.as_view(), name='AllData'),
    path('alldata/message', message, name='message'),


]