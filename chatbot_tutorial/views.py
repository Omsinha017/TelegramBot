from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from result.models import Total_result,Individual_result


def get_message_from_request(request):

    received_message = {}
    decoded_request = json.loads(request.body.decode('utf-8'))
    print(decoded_request)

    if 'message' in decoded_request:
        received_message = decoded_request['message'] 
        received_message['chat_id'] = received_message['from']['id']
        received_from = decoded_request['message']['from']['first_name']

    return received_message, received_from


def send_messages(message, received_from, token):

    jokes = {
         'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""THis is fun""",
                    """THis isn't fun"""] 
    }

    post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)

    result_message = {}        
    result_message['chat_id'] = message['chat_id']
    indvi_obj, created = Individual_result.objects.get_or_create(user_id=message['chat_id'],name=received_from)
    if len(Total_result.objects.all()) == 0:
        Total_result.objects.create(
                    stupid = 0,
                    fat = 0,
                    dumb = 0
                )
    try:
        total_obj = Total_result.objects.first()
        
        if 'fat' in message['text'].lower():
            total_obj.fat += 1
            indvi_obj.fat += 1
            result_message['text'] = random.choice(jokes['fat'])
            

        elif 'stupid' in message['text'].lower():
            
            total_obj.stupid += 1
            indvi_obj.stupid += 1
            result_message['text'] = random.choice(jokes['stupid'])

        elif 'dumb' in message['text'].lower():
            
            total_obj.dumb += 1
            indvi_obj.dumb += 1
            result_message['text'] = random.choice(jokes['dumb'])

        else:
            result_message = {}
            result_message ={  
                "chat_id" : message['chat_id'],
                "text": "Hi {}, Please select an option".format(received_from),
                "reply_markup":{
                    "keyboard":
                    [
                        [
                            {"text":"fat"}
                        ],[
                            {"text":"stupid"}
                        ],[
                            {"text":"dumb"}
                        ]
                    ],
                    "one_time_keyboard" : True
                    }
                }
        total_obj.save()
        indvi_obj.save()
        response_msg = json.dumps(result_message)
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    except:
        pass


class TelegramBotView(generic.View):

    # csrf_exempt is necessary because the request comes from the Telegram server.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    # Post function to handle messages in whatever format they come
    def post(self, request, *args, **kwargs):
        TELEGRAM_TOKEN = '1914384802:AAGSEQuGevuT5VdEZXqMegdYY9aV65MntDo'
        message, received_from = get_message_from_request(request)
        send_messages(message, received_from, TELEGRAM_TOKEN)
        return HttpResponse()
