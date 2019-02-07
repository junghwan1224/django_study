from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import MainTheme, SellPost, PurchasePost
# Create your views here.


def category_list(request):
    main = get_object_or_404(MainTheme, pk=1)
    print(main)
    print(main.related_mid_theme.all())
    ctx = {
        'mainTheme': main,
    }
    return render(request, 'c_list.html', ctx)


def sell_post(request, pk):
    sell = get_object_or_404(SellPost, pk=pk)
    return render(request, 'sell_post.html', {'sell_post': sell})


def purchase_post(request, pk):
    purchase = get_object_or_404(PurchasePost, pk=pk)
    return render(request, 'purchase_post.html', {'purchase_post': purchase})
