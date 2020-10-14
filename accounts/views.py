from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import ProductFilter, CustomerFilter, IssueOrderFilter, ReturnOrderFilter


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        data = {'customers': customers}
        pdf = render_to_pdf('accounts/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        data = {'customers': customers}
        pdf = render_to_pdf('accounts/pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


class ViewPDFBook(View):
        def get(self, request, *args, **kwargs):
            products = Product.objects.all()
            data = {'products': products}
            pdf = render_to_pdf('accounts/book_pdf_template.html', data)
            return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDFBook(View):
        def get(self, request, *args, **kwargs):
            products = Product.objects.all()
            data = {'products': products}
            pdf = render_to_pdf('accounts/book_pdf_template.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response


class ViewPDFOrder(View):
    def get(self, request, *args, **kwargs):
        orders = IssueOrder.objects.all()
        data = {'orders': orders}
        pdf = render_to_pdf('accounts/order_pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDFOrder(View):
    def get(self, request, *args, **kwargs):
        orders = IssueOrder.objects.all()
        data = {'orders': orders}
        pdf = render_to_pdf('accounts/order_pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


@login_required(login_url='login')
def home(request):
    books = Product.objects.all()
    issueOrders = IssueOrder.objects.all()
    returnOrders = ReturnOrder.objects.all()
    customers = Customer.objects.all()
    products = Product.objects.all()

    total_books = Product.objects.count()
    books_out = IssueOrder.objects.filter(status='Checked Out').count()
    books_in = ReturnOrder.objects.filter(status='Checked In').count()

    context = {'books': books, 'issueOrders': issueOrders, 'returnOrders': returnOrders, 'customers': customers, 'products': products,
               'total_books': total_books, 'books_out': books_out,
               'books_in': books_in}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def admin(request):
    return render(request)


@login_required(login_url='login')
def customer(request):
    customers = Customer.objects.all()

    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs

    context = {'customers': customers, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def product(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'accounts/products.html', context)


@login_required(login_url='login')
def issueOrder(request):
    issueOrders = IssueOrder.objects.all()

    myFilter = IssueOrderFilter(request.GET, queryset=issueOrders)
    issueOrders = myFilter.qs

    context = {'issueOrders': issueOrders, 'myFilter': myFilter}
    return render(request, 'accounts/order.html', context)


@login_required(login_url='login')
def returnOrder(request):
    returnOrders = ReturnOrder.objects.all()

    myFilter = ReturnOrderFilter(request.GET, queryset=returnOrders)
    returnOrders = myFilter.qs

    context = {'returnOrders': returnOrders, 'myFilter': myFilter}
    return render(request, 'accounts/order.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)
