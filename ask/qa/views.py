from django.http import HttpResponse
from django.views.decorators.http import require_GET

def test(request,*args,**kwargs):
	return HttpResponse('OK')

@require_GET
def questions_list(request):
    request.GET.get('page')