from typing import List

from core.utills import response
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router
from realty.schemas import RealtyTypeSchema, RealtyTypeInSchema

from core import status
from realty.models import RealtyType

realty = Router(tags=["RealtyType"])


@realty.get("", response=List[RealtyTypeSchema])
def get_realty_type_list(request):
    return get_list_or_404(RealtyType)


@realty.post("", description="")
def create_realty_type(request, realty_type: RealtyTypeInSchema):
    query = RealtyType.objects.create(**realty_type.dict())
    return {"id": query.id}


@realty.put("/{type_id}")
def update_realty_type(request, type_id: int, realty_type: RealtyTypeInSchema):
    query = get_object_or_404(RealtyType, id=type_id)
    for attr, value in realty_type.dict().items():
        setattr(query, attr, value)
    query.save()
    return response(status.HTTP_200_OK, {'message': 'updated successfully'})


@realty.delete("/{type_id}")
def delete_realty_type(request, type_id: int):
    realty_type = get_object_or_404(RealtyType, id=type_id)
    realty_type.delete()
    return response(status.HTTP_200_OK, {'message': 'deleted successfully'})
