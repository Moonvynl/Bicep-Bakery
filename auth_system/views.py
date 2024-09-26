from django.contrib.auth import login
from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth_system/register.html'
    success_url = reverse_lazy('shop:general')
    def form_valid(self, form):
        user = form.save()
    
        if user:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            if user.is_authenticated:
                return HttpResponseRedirect(self.success_url)
            else:
                return redirect("auth_system:login")

        return super().form_valid(form)