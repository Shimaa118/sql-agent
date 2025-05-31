from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class SalesData(Base):
    __tablename__ = 'sales_data'
    date = Column(String, primary_key=True)
    total_sales_amount = Column(Float)
    total_units_sold = Column(Integer)

class ProductCatalog(Base):
    __tablename__ = 'product_catalog'
    product_id = Column(String, primary_key=True)
    category = Column(String)
    name = Column(String)
    price = Column(Float)
    stock_level = Column(Integer)

def setup_database(db_url='sqlite:///mydatabase.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        if not session.query(SalesData).first():
            session.add_all([
                SalesData(date='2023-09-28', total_sales_amount=5000, total_units_sold=100),
                SalesData(date='2023-09-29', total_sales_amount=10000, total_units_sold=250),
                SalesData(date='2023-09-30', total_sales_amount=8000, total_units_sold=200)
            ])

            session.add_all([
                ProductCatalog(product_id='E1001', category='Electronics', name='Smartphone', price=500, stock_level=20),
                ProductCatalog(product_id='E1002', category='Electronics', name='Laptop', price=1000, stock_level=15),
                ProductCatalog(product_id='E1003', category='Electronics', name='Tablet', price=300, stock_level=25),
                ProductCatalog(product_id='C1001', category='Clothing', name='T-Shirt', price=20, stock_level=100),
                ProductCatalog(product_id='C1002', category='Clothing', name='Jeans', price=50, stock_level=80),
                ProductCatalog(product_id='C1003', category='Clothing', name='Jacket', price=100, stock_level=40)
            ])
            session.commit()
    return engine
