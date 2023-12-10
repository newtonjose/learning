# country
# states
# cites
from typing import Optional, List

from sqlmodel import Field, SQLModel

from customers.domain.models import Addresses


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    # addresses: Optional[List[Addresses]] = Field(default=list)
