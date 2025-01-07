from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/merchant/')
async def get_merchant(db: Session = Depends(get_db)):
    try:
        return await service.get_merchant(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchant/id')
async def get_merchant_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_merchant_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/merchant/')
async def post_merchant(id: str, merchant_id: str, name: str, token: str, merchant_code: str, address: str, status: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.post_merchant(db, id, merchant_id, name, token, merchant_code, address, status, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/merchant/id/')
async def put_merchant_id(id: str, merchant_id: str, name: str, token: str, merchant_code: str, address: str, status: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_merchant_id(db, id, merchant_id, name, token, merchant_code, address, status, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/merchant/id')
async def delete_merchant_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_merchant_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchant_rate_slab_master/')
async def get_merchant_rate_slab_master(amount: int, db: Session = Depends(get_db)):
    try:
        return await service.get_merchant_rate_slab_master(db, amount)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchant_rate_slab_master/id')
async def get_merchant_rate_slab_master_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_merchant_rate_slab_master_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/merchant_rate_slab_master/')
async def post_merchant_rate_slab_master(id: str, merchant_id: str, slab_from: str, slab_to: str, base_amount: str, emi_amount: str, emi_tenure: str, processing_fee: str, effective_date: str, expiry_date: str, remarks: str, status: str, created_at: str, updated_at: str, cgst: str, igst: str, scst: str, gst: str, convenience_charges: str, db: Session = Depends(get_db)):
    try:
        return await service.post_merchant_rate_slab_master(db, id, merchant_id, slab_from, slab_to, base_amount, emi_amount, emi_tenure, processing_fee, effective_date, expiry_date, remarks, status, created_at, updated_at, cgst, igst, scst, gst, convenience_charges)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/merchant_rate_slab_master/id/')
async def put_merchant_rate_slab_master_id(id: str, merchant_id: str, slab_from: str, slab_to: str, base_amount: str, emi_amount: str, emi_tenure: str, processing_fee: str, effective_date: str, expiry_date: str, remarks: str, status: str, created_at: str, updated_at: str, cgst: str, igst: str, scst: str, gst: str, convenience_charges: str, db: Session = Depends(get_db)):
    try:
        return await service.put_merchant_rate_slab_master_id(db, id, merchant_id, slab_from, slab_to, base_amount, emi_amount, emi_tenure, processing_fee, effective_date, expiry_date, remarks, status, created_at, updated_at, cgst, igst, scst, gst, convenience_charges)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/merchant_rate_slab_master/id')
async def delete_merchant_rate_slab_master_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_merchant_rate_slab_master_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

