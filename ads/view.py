from django.http import JsonResponse


def status(request):
    return JsonResponse({"status": "ok"}, status=200)
