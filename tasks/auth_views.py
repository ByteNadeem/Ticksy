from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from allauth.account.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    """Custom login view that adds success message"""
    def form_valid(self, form):
        response = super().form_valid(form)
        username = self.request.user.username
        messages.success(
            self.request,
            f'Welcome back, {username}! You have successfully logged in.'
        )
        return response


class CustomLogoutView(LogoutView):
    """Custom logout view that adds goodbye message"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            response = super().dispatch(request, *args, **kwargs)
            messages.info(
                request,
                f'Goodbye, {username}! You have been successfully logged out.'
            )
            return response
        return super().dispatch(request, *args, **kwargs)


@csrf_protect
@require_http_methods(["GET", "POST"])
def custom_logout_view(request):
    """Simple logout view with message - handles both GET and POST"""
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)
            messages.info(
                request,
                f'Goodbye, {username}! You have been successfully logged out.'
            )
        return redirect('home')
    else:
        # For GET requests, render logout confirmation
        return redirect('account_logout')
