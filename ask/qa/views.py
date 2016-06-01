from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime, timedelta

from qa.forms import AskForm, AnswerForm, SignupForm, ProfileForm
from qa.models import Question, Answer, Profile, paginate

import json


def test(request, *args, **kwargs):
    return HttpResponse('OK')


class HttpResponseAjax(HttpResponse):
    def __init__(self, status='ok', **kwargs):
        kwargs['status'] = status
        super(HttpResponseAjax, self).__init__(content=json.dumps(kwargs), content_type='application/json')


class HttpResponseAjaxError(HttpResponseAjax):
    def __init__(self, code, message):
        super(HttpResponseAjaxError, self).__init__(status='error', code=code, message=message)


@require_GET
def questions_list(request):
    qs = Question.objects.order_by('-id')
    questions = paginate(request, qs.all())
    return render(request, 'qa/question_list.html', {
        "questions": questions,
    })


@require_GET
def popular_questions(request):
    qs = Question.objects.filter(added_at__gte=datetime.today() - timedelta(days=7))
    qs = qs.order_by('-rating')
    questions = paginate(request, qs.all())
    return render(request, 'qa/question_list.html', {
        "questions": questions
    })


def question_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    answers = Answer.objects.filter(question=question)
    answers=answers.order_by('-correct','id').all()
    form = AnswerForm(initial={'question': pk})
    return render(request, 'qa/question_detail.html', {
        "question": question,
        "answers": answers,
        "form": form,
    })


@login_required(login_url='/login/')
def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form
    })


@require_POST
@login_required(login_url='/login/')
def answer_add(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/', request)

    form = AnswerForm(request.POST)
    if form.is_valid():
        form._user = request.user
        answer = form.save()
        return HttpResponseRedirect(answer.get_url())
    return HttpResponseRedirect('/question/%s/' % request.POST['question'])


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form
    })


def settings_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form._user = request.user
            profile = form.save()
            HttpResponseRedirect('/settings/')
    else:
        form = ProfileForm(initial={
            'username': profile.user.username,
            'email': profile.user.email,
            'nick_name': profile.nick_name,
            'avatar': profile.avatar,
            'password': profile.user.password
        })
    return render(request, 'qa/profile.html', {
        'form': form,
        'avatar': profile.avatar
    })

@csrf_protect
def like(request):
    id=request.POST['question_id']
    question = Question.objects.get(id=id)
    if question.author_id != request.user.id:
        if not question.likes.filter(id=request.user.id).exists():
            question.likes.add(request.user)
            question.rating += 1
            question.save()
    return HttpResponseAjax(rating=question.rating)


def correct_answer(request, question_id, answer_id):
    answers = Answer.objects.filter(question_id=question_id)
    answers = answers.all()
    answer_id=int(answer_id)
    for answer in answers:
        if answer.id == answer_id:
            if not answer.correct:
                answer.correct = True
                answer.save()
        elif answer.correct:
            answer.correct = False
            answer.save()
    return HttpResponseRedirect('/question/' + question_id)
