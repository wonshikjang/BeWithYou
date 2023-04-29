from datetime import datetime
from typing import Optional

from pydantic import BaseModel



"""
Post 테이블 schema
"""


class BasePost(BaseModel):
    user_name: str
    ans_1: Optional[str]
    ans_2: Optional[str]
    ans_3: Optional[str]
    ans_4: Optional[str]
    ans_5: Optional[str]
    keyword: Optional[str]

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
    keyword: Optional[str]
    class Config:
        orm_mode = True
