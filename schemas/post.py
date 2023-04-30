from datetime import datetime
from typing import Optional

from pydantic import BaseModel



"""
Post 테이블 schema
"""


class BasePost(BaseModel):
    user_name: str
    ans_1: str
    ans_2: str
    ans_3: str
    ans_4: str
    ans_5: str
    ans_6: str
    ans_7: str
    keyword: Optional[str]
    touch: Optional[str]
    shared: Optional[int]


    class Config:
        orm_mode = True


class ReadPost(BasePost):
    user_id: int
    create_time: datetime
    update_time: datetime



class PatchPost(BaseModel):
    user_name: Optional[str]
    ans_1: Optional[str]
    ans_2: Optional[str]
    ans_3: Optional[str]
    ans_4: Optional[str]
    ans_5: Optional[str]
    ans_6: Optional[str]
    ans_7: Optional[str]
    keyword: Optional[str]
    touch: Optional[str]
    shared: Optional[int]
    class Config:
        orm_mode = True
