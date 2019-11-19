from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):

    def test_fun(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")

        
class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")
    