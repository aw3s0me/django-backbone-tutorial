from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question

def index(request):
	latest_poll_list = Question.objects.all()#Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.question_text for p in latest_poll_list])
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))
	#return HttpResponse(output)
	#return HttpResponse("Hello, world. Poll index")

def detail(request, poll_id):
	try:
		poll = Question.objects.get(pk=poll_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})
    #return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)



# Create your views here.
