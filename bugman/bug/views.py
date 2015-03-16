from django.shortcuts import render

# Create your views here.

# stores bug in db
def report_bug(request, template='bug/report_bug.html'):
	return render(request, template)