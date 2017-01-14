from django.shortcuts import render
from django.http import JsonResponse
from models import Company, Reviewer, Review
import json

def index(request):
	return render(request, 'review_api/index.html')

def register(request):
	if request.method == "POST":
		if 'HTTP_SOURCE' in request.META:
			if request.META['HTTP_SOURCE'] == 'website':
				data = json.loads(request.body)
				create = Reviewer.objects.create(data)
				return JsonResponse(create)
		else:
			create = Reviewer.objects.create(request.POST.copy())
			return JsonResponse(create)
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

