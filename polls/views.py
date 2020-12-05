from django.http import HttpResponse

HASH="9cbe38ee"

def index(request):
    return HttpResponse(f"Hello, world {HASH}. You're at the polls index.")
