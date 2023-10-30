
import datetime
import random
from .forms import ImageForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import SaveCoin,Product, Сlient, Order
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("About us")

def coin(request):
    rnd_coin = random.choice(["Орел","Решка"])
    save_coin = SaveCoin(coin_var=rnd_coin)
    save_coin.save()
    return HttpResponse(rnd_coin)

def get_all_coin(request):
    return HttpResponse(SaveCoin.get_n(4))

def get_user_products(request,user_id,days):
    
    client = get_object_or_404(Сlient, pk=user_id)
    orders = Order.objects.filter(client=client).order_by('-id')

    result = []
    for order in orders:
        if order.date > (datetime.datetime.now() - datetime.timedelta(days=days)).replace(tzinfo=datetime.timezone.utc):
            if order.product.name is not result: result.append(order.product.name)
    context = {"name": client.name,"products":result,"days":days}
    return render(request, "app1/get_user_prod.html", context)

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data['id']
            product = get_object_or_404(Product, pk=id)
            product.image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(product.image.name, product.image)
    else:
        form = ImageForm()
    return render(request, 'app1/upload_image.html', {'form':form})