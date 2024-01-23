from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column 
from sqlalchemy.schema import MetaData

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/test_database")

con = engine.connect()


result = con.execute(text('select * from cars'))
for i in result:
    print(i)

# trans = con.begin()
# try:
#     con.execute("INSERT INTO CARS (car_name,volume) VALUES (%s, %s)", ("Bentley", 6))
#     trans.commit();
# except Exception as e:
#     trans.rollback();
#     print(e)

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, primary_key=True)
    car_name = Column(String)
    volume = Column(Integer)

Base.metadata.create_all(engine)
Sessions = sessionmaker(bind=engine)
session = Sessions()

# car = Car(car_id = 6, car_name = 'Hunday', volume = 2)
# session.add(car)
# session.commit()

for i in session.query(Car).order_by('volume'):
    print(i.car_name, '',i.volume)

