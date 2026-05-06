from fastapi import APIRouter, Query
import logging
log = logging.getLogger(__name__)
router = APIRouter()

def get_total(costs:dict, items:list[str], tax:float) -> float:
    bill = [costs.get(item, 0) for item in items]
    total_price = sum(bill) * (1+tax)
    return round(total_price, 2)

@router.get("")
async def total(costs:dict,  tax:float|None = None, items:list[str]|None = Query(None)):
    print(f"Items: {items}, Tax: {tax}, Costs: {costs}")
    if not items or not tax or not costs:
        return {"message": "Missing parameters"}
    total_price = get_total(costs, items, tax)
    return {"Total": total_price}