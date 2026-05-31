from pydantic import BaseModel, Field, AnyUrl
from typing import Annotated, List, Literal, Optional
from uuid import UUID
from datetime import datetime


class Product(BaseModel):
    id: UUID
    sku: Annotated[
        str,
        Field(
            min_length=6,
            max_length=30,
            title="SKU",
            description="Stock Keeping Unit",
            examples=["734-hjd-378-3d", "ONEP-256GB-051"],
        ),
    ]
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=80,
            title="Product Name",
            description="Readable name of the product",
            examples=["OnePlus 11 Pro", "Apple iPhone 15 Pro Max"],
        ),
    ]
    description: Annotated[
        str,
        Field(
            max_length=200,
            title="Product Description",
            description="Detailed information about the product",
        ),
    ]
    category: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            title="Category",
            description="Product category",
            examples=["Smartphones", "Laptops"],
        ),
    ]
    brand: Annotated[
        str,
        Field(
            min_length=2,
            max_length=50,
            title="Brand",
            description="Product brand",
            examples=["OnePlus", "Apple"],
        ),
    ]
    price: Annotated[float, Field(gt=0, strict=True, description="Base price (INR)")]
    currency: Literal["INR"] = "INR"
    discount_percent: Annotated[
        float, Field(ge=0, le=90, description="Discount percentage(0-90)")
    ] = 0
    stock: Annotated[int, Field(ge=0, description="Available stock quantity")]
    is_active: Annotated[bool, Field(description="Is the product active for sale?")]
    rating: Annotated[
        float,
        Field(ge=0, le=5, strict=True, description="Average customer rating (0-5)"),
    ]
    tags: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=10, description="Up to 10 tags"),
    ]
    image_url: Annotated[
        List[AnyUrl], Field(max_length=1, description="Atleast 1 link")
    ]

    # dimensions_cm

    # seller

    created_at: datetime
