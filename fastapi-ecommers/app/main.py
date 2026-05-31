from fastapi import FastAPI, HTTPException, Query, Path
from service.products import get_all_products
from schema.product import Product

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}


# @app.get('/products')
# def get_products():
#     return get_all_products()


@app.get("/products")
def list_products(
    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by Product Name (case insensitive)",
    ),
    sort_by_price: bool = Query(default=False, description="Sort products by price"),
    order: str = Query(
        default="asc", description="Sort order when sort_by_price=true (asc, desc)"
    ),
    limit: int = Query(
        default=10, ge=1, le=100, description="Number of items to return"
    ),
):

    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail=f"No product found matching name={name}"
        )

    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    products = products[0:limit]
    total = len(products)

    return {"total": total, "items": products}


@app.get("/products/{product_id}")
def get_product_by_id(
    product_id: str = Path(
        ...,
        description="The ID of the product to retrieve",
        min_length=36,
        max_length=36,
        examples="2e64ac5f-5859-4212-a0e8-36b8a42844ad",
    )
):
    products = get_all_products()
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def create_product(product: Product):
    return product
