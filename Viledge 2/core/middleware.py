from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def villager_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_villager:
            return redirect("villager_login")  # Redirect unauthorized access
        return view_func(request, *args, **kwargs)
    return wrapper

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            return redirect("admin_login")  # Redirect unauthorized access
        return view_func(request, *args, **kwargs)
    return wrapper
