from django.conf.urls import patterns, include, url
from authorize import views

urlpatterns = patterns(
    '',
    url(r'^signup/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
)
