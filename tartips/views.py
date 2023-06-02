from django.shortcuts import render

# Create your views here.

def main(request):
    '''
    Args: None
    Process:None
    Return:Devuelve el render de la pagina principal.
    '''
    return render(request,'main.html')