"""Cabify data model definition."""

from sqlalchemy import Column, Float, String, UniqueConstraint, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PedidosYa(Base):
    """Cabify data model."""

    __tablename__ = "cabify_rides"

    __table_args__ = (UniqueConstraint("id"),)

    id = Column(Integer)
    date = Column(TIMESTAMP)
    base_price = Column(Float)
    processing_fee = Column(Float)
    high_demand_fee = Column(Float)
    total_price = Column(Float)
    trip_duration = Column(Float)

    __mapper_args__ = {"primary_key": [id]}

    def __init__(
        self,
        id,
        date,
        base_price,
        processing_fee,
        high_demand_fee,
        total_price,
        trip_duration,
    ):
        self.id = id
        self.date = date
        self.base_price = base_price
        self.processing_fee = processing_fee
        self.high_demand_fee = high_demand_fee
        self.total_price = total_price
        self.trip_duration = trip_duration

    def __repr__(self):
        return f"""
        <StockValue(id='{self.id}', 
                    date='{self.date}', 
                    base_price='{self.base_price}', 
                    processing_fee='{self.processing_fee}, 
                    high_demand_fee='{self.high_demand_fee}', 
                    total_price='{self.total_price}',
                    trip_duration='{self.trip_duration}'
        )>"""
