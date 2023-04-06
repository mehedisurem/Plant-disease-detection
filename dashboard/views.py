from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'dashboard/test.html')


def about(request):
    return render(request, 'dashboard/about.html')


def pdf(request):
    return render(request, 'dashboard/test.html')


def sadia(request):
    return render(request, 'dashboard/sadia.html')


def mehenaz(request):
    return render(request, 'dashboard/mehenaz.html')


def surem(request):
    return render(request, 'dashboard/surem.html')


def istiaq(request):
    return render(request, 'dashboard/istiaq.html')


def rafi(request):
    return render(request, 'dashboard/rafi.html')


def jahedul(request):
    return render(request, 'dashboard/jahedul.html')

def system(request):
    return render(request, 'dashboard/system-Diagram.html')


def hardwere(request):
    return render(request, 'dashboard/hardware-Design.html')

def merge(request):
    return render(request, 'dashboard/merged-summary.html')

def draft(request):
    return render(request, 'dashboard/draft.html')

def survey_form(request):
    return render(request, 'dashboard/survey-form.html')

def survey_ques(request):
    return render(request, 'dashboard/survey-questions.html')

def survey_doc(request):
    return render(request, 'dashboard/documentation.html')

def esp(request):
    return render(request, 'dashboard/esp.html')


@csrf_exempt
def AIresponse(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        if input_text:
            # Define the API endpoint URL and headers
            # url = "https://api.openai.com/v1/engines/curie/completions"
            # url = "https://api.openai.com/v1/engines/davinci-codex/completions"
            # url = "https://api.openai.com/v1/engines/davinci/completions"
            url = "https://api.openai.com/v1/engines/davinci/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer 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"
            }

            # Define the request payload
            data = {
                "prompt": input_text,
                "max_tokens": 200,
                "temperature": 0.5
            }

            # Send the request to the OpenAI API
            response = requests.post(url, headers=headers, json=data)

            # Process the response data and return it as a JSON response
            response_json = response.json()
            # print(response_json)
            generated_text = response_json["choices"][0]["text"] if "choices" in response_json else response_json.get(
                "text", "")
            print('Generated text:', generated_text)

            return render(request, 'dashboard/AIresponse.html', {'generated_text': generated_text})

            # return render(request, 'dashboard/AIresponse.html', {'generated_text': generated_text})

        # Return an error response if input_text is not provided
        else:
            return JsonResponse({'error': 'Bad request'}, status=400)
    else:
        return render(request, 'dashboard/AIresponse.html')

    # Return a bad request error if the request method is not POST or input_text is not provided
