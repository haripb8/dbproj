from django.urls import path
from.import views
urlpatterns=[
    path('',views.f,name='f'),
    path('f1',views.f1,name='f1'),
    path('f2',views.f2,name='f2'),
    path('f3',views.f3,name='f3'),
    path('f4',views.f4,name='f4'),
    path('f5',views.f5,name='f5')

]