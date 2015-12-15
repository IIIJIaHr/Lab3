from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/register/login/'

    template_name = 'register/signup.html'

    def form_valid(self, form):
        form.save()
        print 'valid'
        return super(RegisterFormView, self).form_valid(form)




class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'register/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
