from django.shortcuts import render

# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'encuesta/index.html',context)
def detalle(request,pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    context = {
        'pregunta':pregunta
    }
    
    return render(request,'encuesta/detalle.html',context)
