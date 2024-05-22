import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from .models import (Image, Product_category_1, Product_category_2, Product,
                     AboutUs, Work, Employee, Import, Exsport, Outsourcing,
                     CustomsClearance, Xabar, Hamkor, New, PressCenter_1, PressCenter_2, AppealOfLegal, PhotoGallery,
                     VideoGallery, Corruption, CompanyDetails, Contact, Telegram)
from django.utils.translation import get_language, activate


def send_to_telegram(message, apiToken, chatID):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        pass


def set_language(request, id):
    if id == 1:
        activate('uz')

    elif id == 2:
        activate('ru')
    else:
        activate('en')
    return redirect(index)


def index(request):
    context = {
        'language': get_language(),
        'main_images': Image.objects.all().order_by('-id')[0:3],
        "press_center": PressCenter_1.objects.all().order_by('-id'),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'products_c_2': Product_category_2.objects.all().order_by('-id')[:4],
        "about_us_item": AboutUs.objects.first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
    }
    return render(request, 'index.html', context)


def about_us(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "about_us_items": AboutUs.objects.all().order_by('-id')
    }
    return render(request, 'about-us.html', context)


def works(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "work_items": Work.objects.all().order_by('-id')
    }
    return render(request, 'works.html', context)


def employee(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "employee_items": Employee.objects.all().order_by('-id')
    }
    return render(request, 'employee.html', context)


def products(request, id):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "product_c_1": Product_category_1.objects.get(id=id),
        'products_c_2': Product_category_2.objects.filter(Type_1=id).order_by('-id'),
    }
    return render(request, 'products.html', context)


def product_kategory(request, id):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'product_c_2': Product_category_2.objects.get(id=id),
        'products': Product.objects.filter(Type_2=id).order_by('-id'),
    }
    return render(request, 'products.html', context)


def product_kategory_detail(request, id):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'product': Product.objects.get(id=id),
    }
    return render(request, 'product-detail.html', context)


def services(request, id):
    if id == 1:
        context = {
            'main_images': Image.objects.all().order_by('-id')[0:3],
            'language': get_language(),
            "company": CompanyDetails.objects.all().order_by('-id').first(),
            "hamkorlar": Hamkor.objects.all().order_by('-id'),
            'products_c_1': Product_category_1.objects.all().order_by('-id'),
            "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
            'services_items': Exsport.objects.all().order_by('-id')
        }
    elif id == 2:
        context = {
            'main_images': Image.objects.all().order_by('-id')[0:3],
            'language': get_language(),
            "company": CompanyDetails.objects.all().order_by('-id').first(),
            "hamkorlar": Hamkor.objects.all().order_by('-id'),
            'products_c_1': Product_category_1.objects.all().order_by('-id'),
            "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
            'services_items': Import.objects.all().order_by('-id')}
    elif id == 3:
        context = {
            'main_images': Image.objects.all().order_by('-id')[0:3],
            'language': get_language(),
            "company": CompanyDetails.objects.all().order_by('-id').first(),
            "hamkorlar": Hamkor.objects.all().order_by('-id'),
            'products_c_1': Product_category_1.objects.all().order_by('-id'),
            "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
            'services_items': CustomsClearance.objects.all().order_by('-id')}
    else:
        context = {
            'main_images': Image.objects.all().order_by('-id')[0:3],
            'language': get_language(),
            "company": CompanyDetails.objects.all().order_by('-id').first(),
            "hamkorlar": Hamkor.objects.all().order_by('-id'),
            'products_c_1': Product_category_1.objects.all().order_by('-id'),
            "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
            'services_items': Outsourcing.objects.all().order_by('-id')}
    return render(request, 'xizmatlar.html', context)


def message(request):
    next = request.POST.get('next', '/')
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Sxbteams.uz saytingidan xabar'
        if name:
            for acount in Telegram.objects.all():
                send_to_telegram(f"{subject}\nIsm: {name}\nEmail: {email}\nXabar: {message}", acount.apiToken,
                                 acount.chatID)
            Xabar.objects.create(User=name, Email=email, Message=message)
        messages.success(request, "Muvaffaqiyatli yuborildi!")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return redirect('index')


def news(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "news": New.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
    }
    return render(request, 'news.html', context)


def new_details(request, id):
    if New.objects.get(id=id).Video_file == None:
        video_bool = 1
    else:
        video_bool = 2
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "new": New.objects.get(id=id),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'video_bool': video_bool,
    }
    return render(request, 'new-details.html', context)


def press_center_1(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "press_center": PressCenter_1.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'press_center_1': 'press_center_1_details',
    }
    return render(request, 'press-center.html', context)


def press_center_1_details(request, id):
    if PressCenter_1.objects.get(id=id).Video_file == None:
        video_bool = 1
    else:
        video_bool = 2
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "press_center_detail": PressCenter_1.objects.get(id=id),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'video_bool': video_bool,
    }
    return render(request, 'press-center-details.html', context)


def press_center_2(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "press_center": PressCenter_2.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'press_center_2': 'press_center_2_details',
    }
    return render(request, 'press-center.html', context)


def press_center_2_details(request, id):
    if PressCenter_2.objects.get(id=id).Video_file == None:
        video_bool = 1
    else:
        video_bool = 2
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "press_center_detail": PressCenter_2.objects.get(id=id),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        'video_bool': video_bool,
    }
    return render(request, 'press-center-details.html', context)


def feedback(request):
    try:
        data = request.POST
        flexRadioDefault = data.get('flexRadioDefault')
        name = data.get("f-name")
        date = data.get("f-date")
        pasId = data.get("f-pasId")
        address = data.get("f-address")
        index = data.get("f-index")
        email = data.get("f-email")
        phone = data.get("f-phone")
        subject = data.get("f-subject")
        message = data.get("f-message")
        subject = 'Sxbteams.uz saytingidan murojatnoma'
        if name:
            for acount in Telegram.objects.all():
                send_to_telegram(
                    f'{subject}\nIsm: {name}\nEmail: {email}\nPhone: {phone}\nMain subject: {subject}\nXabar: {message}',
                    acount.apiToken, acount.chatID)
            AppealOfLegal.objects.create(Subject=flexRadioDefault, FullName=name, BirthDate=date, PassportData=pasId,
                                         Address=address, Index=index, Email=email, Phone=phone, SubjectType=subject,
                                         QuestionText=message)
        messages.success("Murojatingiz muvaffaqiyatli yuborildi!")
        return render(request, 'feedback.html')


    except:
        pass
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
    }
    return render(request, 'feedback.html', context)


def photo_gallery(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "photo_gallery": PhotoGallery.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
    }
    return render(request, 'photo-gallery.html', context)


def video_gallery(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        "video_gallery": VideoGallery.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
    }
    return render(request, 'video-gallery.html', context)


def corruption(request):
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "corruptions": Corruption.objects.all().order_by('-id')
    }
    return render(request, 'corruption.html', context)


def contact(request):
    next = request.POST.get('next', '/')
    if request.method == 'POST':
        data = request.POST
        name = data.get('modal-name')
        email = data.get('modal-email')
        company = data.get('modal-organization')
        phone = data.get('modal-phone')
        message = data.get('modal-message')
        Contact.objects.create(Name=name, Email=email, Company=company, Phone=phone, Message=message)
        subject = "Sxbteams.uz saytingidan sizga so'rov yuborildi!"
        if name:
            for acount in Telegram.objects.all():
                send_to_telegram(f'{subject}\nIsm: {name}\nEmail: {email}\nPhone: {phone}\nXabar: {message}',
                                 acount.apiToken, acount.chatID)
            messages.success(request, "Muvaffaqiyatli yuborildi!")

        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'main_images': Image.objects.all().order_by('-id')[0:3],
        'language': get_language(),
        "company": CompanyDetails.objects.all().order_by('-id').first(),
        "hamkorlar": Hamkor.objects.all().order_by('-id'),
        'products_c_1': Product_category_1.objects.all().order_by('-id'),
        "products_c_1_2": Product_category_2.objects.all().order_by('-id'),
        "contact": CompanyDetails.objects.all().order_by('-id').first()
    }
    return render(request, 'contact.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)