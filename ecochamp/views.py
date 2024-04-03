import os

from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    #print(request.build_absolute_uri()) #optional
    
    return render(
        request,
        'ecochamp/home.html',
        {
            'name': "Kevin",
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "ecochamp/about.html")

def faq(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'example.txt')
    
    query = request.GET.get('query')
    if query:
        try:
            with open(file_path, 'r') as file:
                matching_lines = []
                for line in file:
                    if query.upper() in line.strip().upper():
                        matching_lines.append(line.strip())
                if matching_lines:
                    context = {
                        'result': matching_lines,
                        'query': query,
                    }
                    # Remove brackets and quotes from each line in the result list
                    context['result'] = [line.strip().strip("[]'") for line in context['result']]
                    return render(request, 'ecochamp/faq.html', context)
                else:
                    return render(request, 'ecochamp/faq.html', {'error': f'No results found for "{query}".'})
        except FileNotFoundError:
            return render(request, 'ecochamp/faq.html', {'error': 'File not found.'})
    return render(request, 'ecochamp/faq.html')