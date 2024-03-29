from fastapi import APIRouter, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List

router = APIRouter(
    prefix="/products", tags=["products"]
)

products = ['watch', 'camera', 'phone']

@router.get('/all')
def get_all_products():

    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get("/withheader")
def get_header(
  response: Response,
  custom_header: Optional[List[str]] = Header(None),
  test_cookie: Optional[str] =Cookie(None)
  ):
    # response.headers["custom_response_header"] = ", ".join(custom_header)
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return {
        "data": response,
        "test_cookie": test_cookie
    }

@router.get('/{id}', responses={
  200: {
    "content": {
      "text/html": {
        "example": "<div>Product</div>"
      }
    },
    "description": "Returns the HTML for an object"
  },
  404: {
    "content": {
      "text/plain": {
        "example": "Product not available"
      }
    },
    "description": "A cleartext error message"
  }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
        <style>
        .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>
        </head>
        <div class="product">{product}</div>
        """
    return HTMLResponse(content=out, media_type="text/html")