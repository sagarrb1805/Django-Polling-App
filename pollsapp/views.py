from django.shortcuts import render
from pollsapp.models import questions
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    polls = questions.objects.all()
    
    return render(request, 'index.html', {'polls': polls})

def vote(request, questionid):        
    question = questions.objects.get(qid=questionid).question
    opt1 = questions.objects.get(qid=questionid).option1
    opt2 = questions.objects.get(qid=questionid).option2
    opt3 = questions.objects.get(qid=questionid).option3
    opt4 = questions.objects.get(qid=questionid).option4
    if request.method == "POST":
        selectedOPtion = request.POST.get('option')
        t = questions.objects.get(qid=questionid)
        if selectedOPtion == "option1":
            t.vote1 = t.vote1 + 1
            t.save()
        elif selectedOPtion == "option2":
            t.vote2 = t.vote2 + 1
            t.save()
        elif selectedOPtion == "option3":
            t.vote3 = t.vote3 + 1
            t.save()
        else:
            t.vote4 = t.vote4 + 1
            t.save()

        return result(request, questionid)
        
    return render(request, 'vote.html', {'question':question, 'opt1':opt1, 'opt2':opt2, 
                                            'opt3':opt3, 'opt4':opt4})

def result(request, questionid):
    question = questions.objects.get(qid=questionid).question
    opt1 = questions.objects.get(qid=questionid).option1
    opt2 = questions.objects.get(qid=questionid).option2
    opt3 = questions.objects.get(qid=questionid).option3
    opt4 = questions.objects.get(qid=questionid).option4
    vote1 = questions.objects.get(qid=questionid).vote1
    vote2 = questions.objects.get(qid=questionid).vote2
    vote3 = questions.objects.get(qid=questionid).vote3
    vote4 = questions.objects.get(qid=questionid).vote4
    totalVote = vote1+vote2+vote3+vote4
    vote1, vote2, vote3, vote4 = round((vote1/totalVote*100), 2), round((vote2/totalVote*100), 2), round((vote3/totalVote*100), 2), round((vote4/totalVote*100), 2)
    
    return render(request, 'result.html', {'question':question, 'opt1':opt1, 'opt2':opt2, 'opt3':opt3, 'opt4':opt4,
                'vote1':vote1, 'vote2':vote2, 'vote3':vote3, 'vote4':vote4})
