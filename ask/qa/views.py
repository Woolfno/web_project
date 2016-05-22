from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from qa.forms import AskForm, AnswerForm
from qa.models import Question
from qa.models import Answer
from qa.models import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def questions_list(request):
    qs = Question.objects.order_by('-added_at')
    questions = paginate(request, qs.all())
    return render(request, 'qa/questions.html', {
        "questions": questions
    })


@require_GET
def popular_questions(request):
    qs = Question.objects.order_by('-rating')
    questions = paginate(request, qs.all())
    return render(request, 'qa/questions.html', {
        "questions": questions
    })


def question_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    answers = Answer.objects.filter(question=question).all()
    form=AnswerForm(initial={'question':pk})
    return render(request, 'qa/question_detail.html', {
        "question": question,
        "answers": answers,
        "form":form,
    })

def question_add(request):
    if request.method=='POST':
        form=AskForm(request.POST)
        if form.is_valid():
            question=form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form=AskForm()
    return render(request,'qa/question_add.html',{
        'form':form
    })

@require_POST
def answer_add(request):
    form=AnswerForm(request.POST)
    if form.is_valid():
        answer=form.save()
        return HttpResponseRedirect(answer.get_url())
    return HttpResponseRedirect('/question/%s/' % request.POST['question'])


def create_question():
    from datetime import datetime
    try:
        create_question.rating += 1
    except AttributeError:
        create_question.rating = 0
    Question.objects.create(title='Q1', text='text1', added_at=datetime.now(), rating=create_question.rating)


def create_answer():
    from datetime import datetime
    questions = Question.objects.all()
    user = User.objects.all()[0]
    for question in questions:
        for x in range(10):
            Answer.objects.create(text=('Answer %d' % x), added_at=datetime.now(), question=question, author=user)


def create_data(request):
    create_question()
    create_answer()
    return questions_list(request)
