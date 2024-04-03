import os

from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

# Handles backend of user homepage
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

# Handles backend of the About Us page
def about(request):
    return render(request, "ecochamp/about.html")

# Handles backend of FAQ page
def faq(request):
    
    # Currently using a text file "example.txt" to test func
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
                    
                    # Removes brackets and quotes from each line in the result list
                    context['result'] = [line.strip().strip("[]'") for line in context['result']]
                    
                    return render(request, 'ecochamp/faq.html', context)
                else:
                    return render(request, 'ecochamp/faq.html', {'error': f'No results found for "{query}".'})
        except FileNotFoundError:
            return render(request, 'ecochamp/faq.html', {'error': 'File not found.'})
    return render(request, 'ecochamp/faq.html')