from rest_framework import routers
from inventory.api import *
from inventory.insertApi import *
from inventory.filterApi import *

router=routers.DefaultRouter()
router.register('api/product',ProductViewSet,'product')
router.register('api/productdetails',ProductDetailsViewSet,'productdetails')
router.register('api/customer',CustomerViewSet,'customer')
router.register('api/order',OrderViewSet,'order')
router.register('api/sales',SalesViewSet,'sales')
router.register('api/payment',PaymentViewSet,'payment')
router.register('api/productlist',ProductList,'ProductList')
router.register('api/productInsertion',ProductInsertion,'Productinsertion')
router.register('api/productDetailsInsertion',ProductDetailsInsertion,'ProductDetailsinsertion')
router.register('api/statusavaliableproducts',StatusAvailableProduct,'StatusAvailableProducts')
router.register('api/priceproductlist',PriceLessProduct,'PriceProductList')
router.register('api/deleteProduct',DeleteProduct,'DeleteProductList')
router.register('api/updateProduct',UpdateRecord,'UpdatedProductList')

urlpatterns = router.urls

