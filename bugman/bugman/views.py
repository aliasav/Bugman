from django.shortcuts import render

def landing_page(request, template='landing_page/home.html'):
	return render(request, template)