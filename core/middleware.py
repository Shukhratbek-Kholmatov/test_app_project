from django.core.exceptions import PermissionDenied
from django_ratelimit.core import is_ratelimited



class GlobalRateLimitMiddleware:
    """
    Butun sayt uchun rate limit middleware.
    Har bir IP uchun 1 daqiqada 100 ta so‘rovdan oshsa, bloklanadi.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.limited = is_ratelimited(
            request, group='global', key='ip', rate='100/m', method=['GET', 'POST'], increment=True
        )
        if request.limited:
            raise PermissionDenied("Siz juda ko‘p so‘rov yubordingiz. Keyinroq urinib ko‘ring.")
        return self.get_response(request)
