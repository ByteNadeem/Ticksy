from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
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


def custom_logout_view(request):
    """Simple logout view with message"""
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(
            request,
            f'Goodbye, {username}! You have been successfully logged out.'
        )
    return redirect('home')
