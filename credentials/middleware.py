
from django.shortcuts import redirect
from django.urls import reverse


class StudentAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        login_url = reverse('credentials:login')

        if not request.user.is_authenticated:
            if request.path != login_url:
                return redirect('credentials:login')

        response = self.get_response(request)

        return response
