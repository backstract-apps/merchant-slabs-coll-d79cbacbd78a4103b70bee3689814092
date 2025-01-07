from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Merchant(BaseModel):
    id: int
    merchant_id: uuid.UUID
    name: str
    token: str
    merchant_code: str
    address: str
    status: int
    created_at: datetime.time
    updated_at: datetime.time


class ReadMerchant(BaseModel):
    id: int
    merchant_id: uuid.UUID
    name: str
    token: str
    merchant_code: str
    address: str
    status: int
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class MerchantRateSlabMaster(BaseModel):
    id: int
    merchant_id: int
    slab_from: Any
    slab_to: Any
    base_amount: Any
    emi_amount: Any
    emi_tenure: int
    processing_fee: Any
    effective_date: datetime.date
    expiry_date: datetime.date
    remarks: str
    status: int
    created_at: datetime.time
    updated_at: datetime.time
    cgst: Any
    igst: Any
    scst: Any
    gst: Any
    convenience_charges: Any


class ReadMerchantRateSlabMaster(BaseModel):
    id: int
    merchant_id: int
    slab_from: Any
    slab_to: Any
    base_amount: Any
    emi_amount: Any
    emi_tenure: int
    processing_fee: Any
    effective_date: datetime.date
    expiry_date: datetime.date
    remarks: str
    status: int
    created_at: datetime.time
    updated_at: datetime.time
    cgst: Any
    igst: Any
    scst: Any
    gst: Any
    convenience_charges: Any
    class Config:
        from_attributes = True


