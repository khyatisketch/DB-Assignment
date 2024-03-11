import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship('Product', back_populates='category')

class ProductInventory(Base):
    __tablename__ = 'product_inventory'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    discount_percent = Column(Numeric)
    active = Column(Boolean)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    SKU = Column(String)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'))
    price = Column(Numeric)
    discount_id = Column(Integer, ForeignKey('discount.id'))
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

    category = relationship('ProductCategory', back_populates='products')
    inventory = relationship('ProductInventory')
    discount = relationship('Discount')

    engine = create_engine('sqlite:///mydatabase.db')
    Base.metadata.create_all(engine)