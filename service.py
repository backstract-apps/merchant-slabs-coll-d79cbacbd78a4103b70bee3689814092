from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_merchant(db: Session):

    merchant_all = db.query(models.Merchant).order_by(models.Merchant.id).all()
    res = {
        'merchant_all': merchant_all,
    }
    return res

async def get_merchant_id(db: Session, id: int):

    merchant_one = db.query(models.Merchant).filter(models.Merchant.id == 'id').first()
    res = {
        'merchant_one': merchant_one,
    }
    return res

async def post_merchant(db: Session, id: str, merchant_id: str, name: str, token: str, merchant_code: str, address: str, status: str, created_at: str, updated_at: str):

    record_to_be_added = {'id': id, 'merchant_id': merchant_id, 'name': name, 'token': token, 'merchant_code': merchant_code, 'address': address, 'status': status, 'created_at': created_at, 'updated_at': updated_at}
    new_merchant = models.Merchant(**record_to_be_added)
    db.add(new_merchant)
    db.commit()
    db.refresh(new_merchant)
    merchant_inserted_record = new_merchant
    res = {
        'merchant_inserted_record': merchant_inserted_record,
    }
    return res

async def put_merchant_id(db: Session, id: str, merchant_id: str, name: str, token: str, merchant_code: str, address: str, status: str, created_at: str, updated_at: str):

    merchant_edited_record = db.query(models.Merchant).filter(models.Merchant.id == id).first()
    for key, value in {'id': id, 'merchant_id': merchant_id, 'name': name, 'token': token, 'merchant_code': merchant_code, 'address': address, 'status': status, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(merchant_edited_record, key, value)
    db.commit()
    db.refresh(merchant_edited_record)
    merchant_edited_record = merchant_edited_record

    res = {
        'merchant_edited_record': merchant_edited_record,
    }
    return res

async def delete_merchant_id(db: Session, id: int):

    merchant_deleted = None
    record_to_delete = db.query(models.Merchant).filter(models.Merchant.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        merchant_deleted = record_to_delete
    res = {
        'merchant_deleted': merchant_deleted,
    }
    return res

async def get_merchant_rate_slab_master(db: Session, amount: int):

    
    from sqlalchemy import and_

    merchant_slabs:Any = None
    
    amount = float(amount)
    
    merchant_slabs = db.query(models.MerchantRateSlabMaster).filter(and_( models.MerchantRateSlabMaster.slab_from <= amount, models.MerchantRateSlabMaster.slab_to >= amount )).order_by(models.MerchantRateSlabMaster.id).all()
    res = {
        'merchant_slabs': merchant_slabs,
    }
    return res

async def get_merchant_rate_slab_master_id(db: Session, id: int):

    merchant_rate_slab_master_one = db.query(models.Merchant_rate_slab_master).filter(models.Merchant_rate_slab_master.id == 'id').first()
    res = {
        'merchant_rate_slab_master_one': merchant_rate_slab_master_one,
    }
    return res

async def post_merchant_rate_slab_master(db: Session, id: str, merchant_id: str, slab_from: str, slab_to: str, base_amount: str, emi_amount: str, emi_tenure: str, processing_fee: str, effective_date: str, expiry_date: str, remarks: str, status: str, created_at: str, updated_at: str, cgst: str, igst: str, scst: str, gst: str, convenience_charges: str):

    record_to_be_added = {'id': id, 'merchant_id': merchant_id, 'slab_from': slab_from, 'slab_to': slab_to, 'base_amount': base_amount, 'emi_amount': emi_amount, 'emi_tenure': emi_tenure, 'processing_fee': processing_fee, 'effective_date': effective_date, 'expiry_date': expiry_date, 'remarks': remarks, 'status': status, 'created_at': created_at, 'updated_at': updated_at, 'cgst': cgst, 'igst': igst, 'scst': scst, 'gst': gst, 'convenience_charges': convenience_charges}
    new_merchant_rate_slab_master = models.Merchant_rate_slab_master(**record_to_be_added)
    db.add(new_merchant_rate_slab_master)
    db.commit()
    db.refresh(new_merchant_rate_slab_master)
    merchant_rate_slab_master_inserted_record = new_merchant_rate_slab_master
    res = {
        'merchant_rate_slab_master_inserted_record': merchant_rate_slab_master_inserted_record,
    }
    return res

async def put_merchant_rate_slab_master_id(db: Session, id: str, merchant_id: str, slab_from: str, slab_to: str, base_amount: str, emi_amount: str, emi_tenure: str, processing_fee: str, effective_date: str, expiry_date: str, remarks: str, status: str, created_at: str, updated_at: str, cgst: str, igst: str, scst: str, gst: str, convenience_charges: str):

    merchant_rate_slab_master_edited_record = db.query(models.Merchant_rate_slab_master).filter(models.Merchant_rate_slab_master.id == id).first()
    for key, value in {'id': id, 'merchant_id': merchant_id, 'slab_from': slab_from, 'slab_to': slab_to, 'base_amount': base_amount, 'emi_amount': emi_amount, 'emi_tenure': emi_tenure, 'processing_fee': processing_fee, 'effective_date': effective_date, 'expiry_date': expiry_date, 'remarks': remarks, 'status': status, 'created_at': created_at, 'updated_at': updated_at, 'cgst': cgst, 'igst': igst, 'scst': scst, 'gst': gst, 'convenience_charges': convenience_charges}.items():
          setattr(merchant_rate_slab_master_edited_record, key, value)
    db.commit()
    db.refresh(merchant_rate_slab_master_edited_record)
    merchant_rate_slab_master_edited_record = merchant_rate_slab_master_edited_record

    res = {
        'merchant_rate_slab_master_edited_record': merchant_rate_slab_master_edited_record,
    }
    return res

async def delete_merchant_rate_slab_master_id(db: Session, id: int):

    merchant_rate_slab_master_deleted = None
    record_to_delete = db.query(models.Merchant_rate_slab_master).filter(models.Merchant_rate_slab_master.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        merchant_rate_slab_master_deleted = record_to_delete
    res = {
        'merchant_rate_slab_master_deleted': merchant_rate_slab_master_deleted,
    }
    return res

