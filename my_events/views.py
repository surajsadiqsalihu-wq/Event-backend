from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to Event API 🚀",
        "status": "running",
        "endpoints": [
            "/admin/",
            "/api/events/",
            "/api/events/public-events/",
            "/api/token/",
        ]
    })