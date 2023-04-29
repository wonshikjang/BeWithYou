from sqlalchemy import VARCHAR, Column, Integer, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

from core.db import Base


class Post(Base):
    __tablename__ = "post"
    user_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_name = Column(VARCHAR(100), nullable=False)
    ans_1 = Column(VARCHAR(1000))
    ans_2 = Column(VARCHAR(1000))
    ans_3 = Column(VARCHAR(1000))
    ans_4 = Column(VARCHAR(1000))
    ans_5 = Column(VARCHAR(1000))
    ans_6 = Column(VARCHAR(1000))
    ans_7 = Column(VARCHAR(1000))
    keyword = Column(VARCHAR(100))
    sum_1 = Column(VARCHAR(1000))
    sum_2 = Column(VARCHAR(1000))
    sum_3 = Column(VARCHAR(1000))
    sum_4 = Column(VARCHAR(1000))
    sum_5 = Column(VARCHAR(1000))
    sum_6 = Column(VARCHAR(1000))
    sum_7 = Column(VARCHAR(1000))
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    mysql_engine = "InnoDB"

