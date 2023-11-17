# from django.db.models import F, Sum
# from django.shortcuts import render
# from django.utils import translation
# from django.views import View
# from home_module.models import MainSlider
# from orders_module.models import Order, OrderDetail
# from products_module.models import ProductCategory, Product
# from sitesite.models import SiteSetting
#
#
# # Create your views here.
#
# class Home(View):
#
#     def get(self, request):
#         latest_products = Product.objects.filter(is_published=True, soft_deleted=False).order_by('-created_at')
#         categories = ProductCategory.objects.prefetch_related('productcategory_set').filter(parent__name=None)
#         slides = MainSlider.objects.all()
#         context = {
#             'latest_products': latest_products,
#             'categories': categories,
#             'slides': slides,
#         }
#
#         return render(request, './index.html', context)
