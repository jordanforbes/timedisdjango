from django.shortcuts import render
from datetime import datetime

def main(request):
    
    current = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(current)
    
    context={
        'time': current
    }
    return render(request, 'index.html', context)
