import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework import status

from mobile_mart_app.models import Mobile


def verify_login(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True


# API to authenticate user(Login)
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if verify_login(request, username, password):
            return JsonResponse({'message': 'Successfully Logged In !!'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Invalid Credentials!!'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


# API to add mobile devices(only for Authenticated User)
@csrf_exempt
@require_POST
def add_mobile_device(request):
    data = json.loads(request.body)
    brand = data.get('brand')
    model = data.get('model')
    colour = data.get('colour')
    price = data.get('price')
    username = data.get('username')
    password = data.get('password')
    if verify_login(request, username, password):
        mobile_obj = Mobile(brand=brand, model=model, colour=colour, price=price)
        mobile_obj.save()
        return JsonResponse({'message': f'Mobile device added successfully: {mobile_obj}'})
    return JsonResponse({'message': 'Invalid Credentials!!'}, status=status.HTTP_401_UNAUTHORIZED)


# API to delete mobile devices(only for Authenticated User)
@csrf_exempt
# @require_POST
@login_required
def delete_mobile_device(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    device_id = data.get('device_id')
    if verify_login(request, username, password):
        Mobile.objects.filter(id=device_id).delete()
        return JsonResponse({'message': 'Mobile device deleted successfully'})
    return JsonResponse({'message': 'Invalid Credentials!!'}, status=status.HTTP_401_UNAUTHORIZED)


# API to list all phones
@csrf_exempt
def list_all_phones(request):
    phones = Mobile.objects.all()

    # Serialize the phones queryset to JSON
    phone_list = []
    for phone in phones:
        phone_list.append({
            'brand': phone.brand,
            'model': phone.model,
            'colour': phone.colour,
            'price': phone.price
        })

    return JsonResponse({'phones': phone_list})


# API to list all phones with filters(filter by Brand,Model,Colour)
@csrf_exempt
def list_phones_with_filters(request):
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    colour = request.GET.get('colour')

    phones = Mobile.objects.all()

    # Apply filters
    if brand:
        phones = phones.filter(brand=brand)
    if model:
        phones = phones.filter(model=model)
    if colour:
        phones = phones.filter(colour=colour)

    # Serialize the phones queryset to JSON
    phone_list = []
    for phone in phones:
        phone_list.append({
            'brand': phone.brand,
            'model': phone.model,
            'colour': phone.colour,
            'price': phone.price
        })

    return JsonResponse({'phones': phone_list})


# API to list all phones with price range
@csrf_exempt
def list_phones_with_price_range(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        phones = Mobile.objects.filter(price__gte=min_price, price__lte=max_price)
    else:
        return JsonResponse({'message': 'Please enter max_price and min_price value'}, status=status.HTTP_400_BAD_REQUEST)

    # Serialize the phones queryset to JSON
    phone_list = []
    for phone in phones:
        phone_list.append({
            'brand': phone.brand,
            'model': phone.model,
            'colour': phone.colour,
            'price': phone.price
        })

    return JsonResponse({'phones': phone_list})


# API to list all phones in ascending or descending order based on user input
@csrf_exempt
def list_phones_ordered(request):
    order_by = request.GET.get('order_by')
    if order_by == 'ascending':
        phones = Mobile.objects.order_by('price')
    elif order_by == 'descending':
        phones = Mobile.objects.order_by('-price')
    else:
        return JsonResponse({'error': 'Invalid order_by value'}, status=status.HTTP_400_BAD_REQUEST)

    # Serialize the phones queryset to JSON
    phone_list = []
    for phone in phones:
        phone_list.append({
            'brand': phone.brand,
            'model': phone.model,
            'colour': phone.colour,
            'price': phone.price
        })

    return JsonResponse({'phones': phone_list})
