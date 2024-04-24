from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email' : data.get('email'),
        'name' : data.get('name'),
        'password' : data.get('password'),
        'password1' : data.get('password1'),
    })

    if form.is_valid():
        form.save()
        #send verification email later.
    else:
        message: 'Error'

    return JsonResponse({'message':message})