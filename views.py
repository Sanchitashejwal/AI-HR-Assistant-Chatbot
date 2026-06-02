import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Resignation

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    try:
        data = json.loads(request.body)
        message = data.get('message', '').lower()
        
        # Simple intent detection
        if any(word in message for word in ['resign', 'quit', 'leave']):
            intent = 'resignation'
            response_text = "I understand you want to resign. Please fill out the resignation form."
            action = 'show_resignation_form'
        else:
            intent = 'general'
            response_text = f"I received: '{message}'. I can help with resignation processes."
            action = 'general_response'
        
        return JsonResponse({
            'response': response_text,
            'intent': intent,
            'action': action
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def submit_resignation(request):
    try:
        data = json.loads(request.body)
        
        # Create resignation record
        resignation = Resignation.objects.create(
            employee_name=data.get('employee_name'),
            employee_id=data.get('employee_id'),
            reason=data.get('reason'),
            project=data.get('project'),
            manager=data.get('manager'),
            people_lead=data.get('people_lead')
        )
        
        return JsonResponse({
            'success': True,
            'message': f'Thank you {data.get("employee_name")}! Resignation submitted successfully.'
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
