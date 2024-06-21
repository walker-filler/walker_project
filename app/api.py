from typing import List
from ninja import NinjaAPI, Router, Schema
from app.schema import ProductSchema
from app.models import Product

api = NinjaAPI(title="Cloud Demo", version="1")
router = Router()


class NotFoundSchema(Schema):
    message: str


@api.get("/products", response=List[ProductSchema])
def products(request):
    return Product.objects.all()


@api.get("/products/{product_id}", response={200: ProductSchema, 404: NotFoundSchema})
def product_detail(request, product_id: int):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return 404, {"message": "Product does not exist"}


api.add_router("", router)
