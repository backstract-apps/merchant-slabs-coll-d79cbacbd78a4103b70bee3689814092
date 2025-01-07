from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Merchant(Base):
    __tablename__ = 'merchant'
    id = Column(Integer, primary_key=True)
    merchant_id = Column(UUID, primary_key=False)
    name = Column(String, primary_key=False)
    token = Column(String, primary_key=False)
    merchant_code = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    status = Column(Integer, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)

class MerchantRateSlabMaster(Base):
    __tablename__ = 'merchant_rate_slab_master'
    id = Column(Integer, primary_key=True)
    merchant_id = Column(Integer, primary_key=False)
    slab_from = Column(String, primary_key=False)
    slab_to = Column(String, primary_key=False)
    base_amount = Column(String, primary_key=False)
    emi_amount = Column(String, primary_key=False)
    emi_tenure = Column(Integer, primary_key=False)
    processing_fee = Column(String, primary_key=False)
    effective_date = Column(Date, primary_key=False)
    expiry_date = Column(Date, primary_key=False)
    remarks = Column(String, primary_key=False)
    status = Column(Integer, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    cgst = Column(String, primary_key=False)
    igst = Column(String, primary_key=False)
    scst = Column(String, primary_key=False)
    gst = Column(String, primary_key=False)
    convenience_charges = Column(String, primary_key=False)

