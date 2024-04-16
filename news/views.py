from django.db.models import Q
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsBD
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .utils import *

def news(request):
    news = NewsBD.objects.order_by('-date')

    page_obj = paginate(request, news, is_elided=True)

    return render(request, 'news/home_news.html', {
        'news': page_obj.object_list,
        'page_obj': page_obj,
    })

@permission_required('news.add_newsbd')
def news_form(request):
    if request.method == 'POST':
        file_save = NewsBDForm(request.POST)
        if file_save.is_valid():
            file_save.save()
            return redirect('news')
    form = NewsBDForm()
    formBD = {'form' : form}
    return render(request, 'news/newsbd_form.html', formBD)

class NewsList(ListView, PaginatePage):
    model = NewsBD
    template_name = 'news/home_news.html'
    context_object_name = 'news'

    extra_context = {
        'title': 'Список новостей'
    }

    allow_empty = True
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.paginate_elided(context)
        return context

    def get_queryset(self):
        return NewsBD.objects.order_by('-date')

class NewsDetail(DetailView):
    model = NewsBD
    template_name = 'news/one_news.html'
    context_object_name = 'one_news'
    pk_url_kwarg = 'id'

class NewsCreate(CreateView):
    model = NewsBD
    form_class = NewsBDForm

    extra_context = {
        'action': 'Создать'
    }

    @method_decorator(permission_required('news.add_newsbd'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class NewsUpdate(UpdateView):
    model = NewsBD
    form_class = NewsBDForm

    extra_context = {
        'action': 'Изменить'
    }

    @method_decorator(permission_required('news.change_newsbd'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class NewsDelete(DeleteView):
    model = NewsBD
    success_url = reverse_lazy('news')

    extra_context = {
        'action': 'Удалить'
    }

    template_name = 'news/newsbd_form.html'

    @method_decorator(permission_required('news.delete_newsbd'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('news')
        messages.error(request, 'Что-то пошло не так')
    else:
        form = LoginForm()
    return render(request, 'news/login.html', {'formLog': form})

@login_required()
def logout_user(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('news')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('news')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'formReg': form})


def search_results(request):
    results =[]
    if request.method == 'GET':
        query = request.GET.get('q')
        results = NewsBD.objects.filter(Q(title__icontains=query)| Q(anons__icontains=query) |
                                        Q(content__icontains=query) | Q(date__icontains=query))
    return render(request, 'news/search.html', {'results': results,
                                                'query': query })

from django.core.mail import send_mail
from django.conf import settings

def contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['recipient']],
                fail_silently=True
            )
            if mail:
                messages.success(request, 'Письмо было успешно отправлено')
                return redirect('email_page')
            else:
                messages.error(request, 'Письмо не было отправлено, повторите попытку позже')
        else:
            messages.warning(request, 'Письмо было заполнено неверно, перепроверьте введённые данные')
    else:
        form = ContactForm()
    return render(request, 'news/email.html', {'form': form})

from django.http import JsonResponse

from .serializers import NewsSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

def test_json(request):
    return JsonResponse({
        'msg': 'фыв asd',
        'email_path': reverse_lazy('email_page'),
        'number': 1,
        'bool': True
    })

@api_view(['GET', 'POST'])
def news_api_list(request, format=None):
    if request.method == 'GET':
        news = NewsBD.objects.all()
        serializer = NewsSerializer(news, many=True)
        # return JsonResponse({'news': serializer.data})
        return Response({'news': serializer.data})
    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def news_api_detail(request, pk, format=None):
    news_obj = get_object_or_404(NewsBD, pk=pk)
    if news_obj:
        if request.method == 'GET':
            serializer = NewsSerializer(news_obj)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = NewsSerializer(news_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Данные были успешно изменены',
                    'news': serializer.data
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            news_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsBD.objects.all()
    serializer_class = NewsSerializer