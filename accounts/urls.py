from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('admin/', views.admin, name="admin"),
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customer/', views.customer, name="customer"),
    path('issue_order/', views.issueOrder, name="issue_order"),
    path('return_order/', views.returnOrder, name="return_order"),

    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    path('pdf_view_books/', views.ViewPDFBook.as_view(), name="pdf_view_books"),
    path('pdf_download_books/', views.DownloadPDFBook.as_view(), name="pdf_download_books"),

    path('pdf_view_orders/', views.ViewPDFOrder.as_view(), name="pdf_view_orders"),
    path('pdf_download_orders/', views.DownloadPDFOrder.as_view(), name="pdf_download_orders"),
]
