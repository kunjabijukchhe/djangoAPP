from django.conf.urls import url
from reviseApp import views

#template tagging

app_name="reviseApp"

urlpatterns=[
    url(r'^user_login',views.user_login,name='user_login'),
    url(r'^other',views.other,name='other'),
]
