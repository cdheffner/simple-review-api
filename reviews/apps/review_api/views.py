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
		return JsonResponse({'errors': ["Invalid Method"]})

def token(request):
	if request.method == "POST":
		if 'HTTP_SOURCE' in request.META:
			if request.META['HTTP_SOURCE'] == 'website':
				data = json.loads(request.body)
				token = Reviewer.objects.retrieveToken(data)
				return JsonResponse(token)
		else:
			token = Reviewer.objects.retrieveToken(request.POST.copy())
			return JsonResponse(token)
	else:
		return JsonResponse({'errors': ["Invalid Method"]})

def create(request):
	if request.method == "POST":
		if 'HTTP_SOURCE' in request.META:
			if request.META['HTTP_SOURCE'] == 'website':
				data = json.loads(request.body)
		else:
			data = request.POST.copy()
		data['ip_address'] = request.META.get('HTTP_X_FORWARDED_FOR')
		if data['ip_address']:
			data['ip_address'] = data['ip_address'].split(", ")[0]
		else:
			data['ip_address'] = request.META.get('REMOTE_ADDR')
		if not 'token' in data:
			return JsonResponse({'errors': ['Missing Authentication Token']})
		auth = Reviewer.objects.authenticate(data['token'])
		if isinstance(auth, dict) and 'errors' in auth:
			return JsonResponse(auth)
		data['reviewer'] = auth
		if not 'company' in data:
			return JsonResponse({'errors': ['Company name is required']})
		comp = Company.objects.findOrCreate(data['company'])
		data['company'] = comp
		status = Review.objects.create(data)
		return JsonResponse(status)
	else:
		return JsonResponse({'errors': ["Invalid Method"]})

def retrieve(request, token):
	auth = Reviewer.objects.authenticate(token)
	if isinstance(auth, dict) and 'errors' in auth:
			return JsonResponse(auth)
	reviews = Review.objects.retrieve(auth)
	return JsonResponse(reviews)

