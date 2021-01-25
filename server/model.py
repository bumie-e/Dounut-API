from typing import Optional

from pydantic import BaseModel, Field

class DoughnutSchema(BaseModel):
    ids: Optional[str]
    name: Optional[str]
    image: Optional[str]
    price: Optional[int]
    description: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "ids": "1",
                "name": "Glaced fritt Doughnut",
                "image": "5677.jpg",
                "price": 750,
                "description": "This doughnut is glaced with icing sugar and fritt. Delicious!"
            }
        }

class UpdateOrderModel(BaseModel):
    ids: Optional[str]
    name: Optional[str]
    image: Optional[str]
    price: Optional[int]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "ids": "7789",
                "name": "Glaced fritt Doughnut",
                "image": "5677.jpg",
                "price": 780,
                "description": "This doughnut is glaced with icing sugar and fritt. Delicious!"
            }
        }
        
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
