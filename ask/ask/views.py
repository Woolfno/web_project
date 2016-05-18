from django.http import Http404

def http404(request,*args,**kwargs):
	raise Http404
