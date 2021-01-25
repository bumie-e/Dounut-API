from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.model import DoughnutSchema
#from server.model import UpdateOrderModel

router = APIRouter()

doughnut = {
    "1":{
         "ids": "1",
         "name": "Glaced fritt Doughnut",
         "image": "5677.jpg",
         "price": 780,
         "description": "This doughnut is glaced with icing sugar and fritt. Delicious!"
    },
    "2":{
         "ids": "7790",
         "name": "Glaced Sprinkle Doughnut",
         "image": "5877.jpg",
         "price": 900,
         "description": "This doughnut is glaced with Sprinkles. Delicious!"
    },
}

@router.get("/")
async def get_doughnuts() -> dict:
    return {
        "data": doughnut
    }

@router.get("/{id}")
async def get_doughnut(id: str) -> dict:
    if int(id) > len(doughnut):
        return {
            "error": "Invalid Doughnut ID"
        }

    for dounut in doughnut.keys():
        if dounut == id:
            return {
                "data": doughnut[dounut]
            }
        
@router.post("/")
async def add_note(dounut: DoughnutSchema = Body(...)) -> dict:
    dounut.ids = str(len(doughnut) + 1)
    doughnut[dounut.ids] = dounut.dict()

    return {
        "message": "Dounut added successfully"
    }

@router.put("/{id}")
def update_doughnut(id: str, donut: DoughnutSchema):
    stored_donut = doughnut[id]
    if stored_donut:
        stored_donut_model = DoughnutSchema(**stored_donut)
        update_data = donut.dict(exclude_unset=True)
        updated_donut = stored_donut_model.copy(update=update_data)
        doughnut[id] = jsonable_encoder(updated_donut)
        return {
            "message": "Donuts updated successfully "
        }
    return {
        "error": "No such with ID passed exists."
    }

@router.delete("/{id}")
def delete_doughnut(id: str) -> dict:
    if int(id) > len(doughnut):
        return {
            "error": "Invalid Doughnut ID"
        }

    for donut in doughnut.keys():
        if donut == id:
            del doughnut[donut]
            return {
                "message": "Donut item deleted"
            }

    return {
        "error": "Donut with {} doesn't exist".format(id)
    }