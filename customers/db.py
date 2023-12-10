import sqlalchemy
from sqlmodel import SQLModel, Session

from customers.data.models.customer import Customer

engine = sqlalchemy.create_engine('sqlite:///customers.db', echo=True)

SQLModel.metadata.create_all(engine)

customer = Customer(name="Deadpond", secret_name="Dive Wilson")

with Session(engine) as session:
    session.add(customer)
    session.commit()
