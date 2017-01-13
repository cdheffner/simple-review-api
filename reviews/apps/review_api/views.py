from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from djang0.http import JsonResponse

def index(request):
	return render(request, 'review_api/index.html')

def register(request):
	if request.method == "POST":
		placeholder = {is_placeholder: True}
		return JsonResponse(placeholder)
	else:
		return redirect(reverse('index'))

def create(request):
	if request.method == "POST":
		placeholder = {is_placeholder: True}
		return JsonResponse(placeholder)
	else:
		return redirect(reverse('index'))

def retrieve(request):
	placeholder = {is_placeholder: True}
	return JsonResponse(placeholder)

