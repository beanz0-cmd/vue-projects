from pydantic import BaseModel


class Device(BaseModel):
    id: int
    name: str
    ip: str
    type: str
