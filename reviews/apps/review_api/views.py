from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.template import RequestContext

def index(request):
	return render_to_response('review_api/index.html', RequestContext(request, {}))

def register(request):
	if request.method == "POST":

		placeholder = {errors: ["this is a placeholder"]}
		return JsonResponse(placeholder)
	else:
		return JsonResponse({errors: ["Invalid Method"]})

def create(request):
	if request.method == "POST":
		placeholder = {errors: ["this is a placeholder"]}
		return JsonResponse(placeholder)
	else:
		return JsonResponse({errors: ["Invalid Method"]})

def retrieve(request):
	placeholder = {errors: ["this is a placeholder"]}
	return JsonResponse(placeholder)

