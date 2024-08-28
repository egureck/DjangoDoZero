from django.forms import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from polls.models import Question
from polls.forms import QuestionForm

#define uma view baseada em funçaõ

def index(request):
    #return HttpResponse('Ola Django - Index')
    #return render(request, 'index.html')
    aviso = 'Aviso importante!!! Essa página não exige login!!!'
    messages.warning(request, aviso) 
    questions = Question.objects.all()
    context = {'all_questions': questions, 'titulo': 'Ultimas Enquetes'}
    return render(request, 'polls/questions.html', context)

#define uma view baseada em funçaõ
@login_required
def ola(request):
    # return HttpResponse('Ola Django - Ola')
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'polls/questions.html', context)

#class QuestionCreateView(LoginRequiredMixin, CreateView):
#    model = Question
#    template_name = 'polls/question_form.html'
#    fields = ('question_text', 'pub_date')
#    success_url = reverse_lazy('index') 
#    sucess_message = 'Pergunta cadastrada com sucesso!'

#    def form_valid(self, form):
#        messages.success(self.request, self.success_message)
#        return super(QuestionCreateView, self).form_valid(form)

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields=('question_text', 'pub_date')
    success_url = reverse_lazy('index')
    success_message = 'Pergunta criada com sucesso.'
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form) 
    
    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs) 
        context['form_title'] = 'Cadastrando nova pergunta!!'
        return context
    
@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] = form
    context['form_title'] = 'Cadastrando nova pergunta - Função!!'
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta cadastrada com sucesso - Função!')
            return redirect('index')
 
    return render(request, 'polls/question_form.html', context)


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('index')
    #fields=('question_text', 'pub_date')
    form_class = QuestionForm
    success_message = 'Pergunta atualizada com sucesso.'
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form) 

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs) 
        context['form_title'] = 'Atualizando a pergunta!!'
        return context

def question_update(request, question_id):
    context = {}
    question = get_object_or_404(Question, id=question_id)
    form = QuestionForm(request.POST or None, instance=question)
    context['form'] = form
    context['form_title'] = 'Atualizando a pergunta. Função!!'

    if request.method == 'POST':
       if form.is_valid():      
          form.save()
          succes_url = reverse_lazy('index')
          messages.success(request, 'Mensagem atualizada com sucesso!!')
          redirect('index')
    return render(request, 'polls/question_form.html', context)
            
    
    
    
    
        
    