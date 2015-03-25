from django.shortcuts import render
from bug.forms import BugForm

# Create your views here.

# stores bug in db
def report_bug(request, template='bug/report_bug.html'):
	form = BugForm()
	if request.method == 'POST':
		context = {
		'form' : form, 
		}
		return render(request, template, context)
	else:
		context = {
		'form' : form, 
		}
		return render(request, template, context)