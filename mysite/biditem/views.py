from django.shortcuts import render
from .models import Biditem
from .choices import district_choices, county_choices
# Create your views here.

def search(request):
    context={
        'county_choices':county_choices,
        'district_choices':district_choices,
    }

    return render(request, 'biditem/search.html', context)


def searchresult(request):
    queryset_list = Biditem.objects.order_by('-letting_date')

    #payitem
    if 'payitem' in request.GET:
        payitem = request.GET['payitem']
        if payitem:
            queryset_list=queryset_list.filter(payitem_number__icontains=payitem)

    #payitemdesc
    if 'payitemdesc' in request.GET:
        payitemdesc = request.GET['payitemdesc']
        if payitemdesc:
            queryset_list=queryset_list.filter(payitem_desc__icontains=payitemdesc)

    #county
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list=queryset_list.filter(county__iexact=county)

    #district
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list=queryset_list.filter(district__iexact=district)

    links = dict()
    for biditem in queryset_list:
        if biditem.contract[0].isdigit():
            itemlength = len(biditem.item)
            cont2 = "0" * (3-itemlength) + biditem.item
            contlink = cont2 + "-" + biditem.contract
        else:
            cont2 = biditem.item[-3:]
            contlink = biditem.contract + "-" + cont2
        links[biditem.contract] = contlink

    # print(links[biditem.contract])

    context={
        'county_choices':county_choices,
        'district_choices':district_choices,
        'biditems':queryset_list,
        'values':request.GET,
        'links':links
    }

    return render(request, 'biditem/searchresult.html', context)
