from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Signup, Patient


class IndexView(generic.ListView):
	model = Question.objects.order_by('-pub_date')[:5]
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	queryset = Question.objects.order_by('-pub_date')[:5]
	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # context_object_name = 'question'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def cleardb(request):
	Signup.objects.all().delete()
	Patient.objects.all().delete()
	return render(request,'polls/index3.html')

def patientlog(request):
	temp = Signup.objects.get(first_name= request.POST['doctor'])
	instance = Patient.objects.create(doctor_name=temp, first_name=request.POST['first'],last_name=request.POST['last'],email=request.POST['mail'],phone_num=request.POST['num'],blood_type=request.POST['blood'],weight=request.POST['weight'],height=request.POST['height'])
	return render(request,'polls/index3.html')

def patient(request):
	return render(request,'polls/index3.html')

def doctor(request):
	return render(request,'polls/index1.html')

def index(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index3.html')

def login(request):
	email = request.POST['mail']
	password = request.POST['pass']
	if len(Signup.objects.filter(email=email,password=password)):
		context = {"patient_list":Signup.objects.get(email=request.POST['mail'])}
		return render(request,'polls/patientlist.html',context)
	else:
		return HttpResponse("<h1>incorrect Username or password</h1>")

def signup(request):
	# Signup.objects.all().delete()
	instance = Signup.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],email=request.POST['mail'],password=request.POST['pass'],phone_num=request.POST['num'])
	return render(request, 'polls/index1.html')
	# return HttpResponseRedirect('/#login') add redirect to login page

# login redirect method not working
# def login(request):
# 	return HttpResponseRedirect(reverse('polls:login'))

# sign up using django forms for later not now
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             passward = form.cleaned_data['password']
#             query = Signup.objects.create(name = name,text = text,)
#             query.save()


# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))