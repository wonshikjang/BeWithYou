from sqlalchemy import VARCHAR, Column, Integer, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

from core.db import Base


class Post(Base):
    __tablename__ = "post"
    user_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_name = Column(VARCHAR(100), nullable=False)
    ans_1 = Column(VARCHAR(500), nullable=False)
    ans_2 = Column(VARCHAR(500), nullable=False)
    ans_3 = Column(VARCHAR(500), nullable=False)
    ans_4 = Column(VARCHAR(500), nullable=False)
    ans_5 = Column(VARCHAR(500), nullable=False)
    ans_5 = Column(VARCHAR(500), nullable=False)
    keyword = Column(VARCHAR(100), nullable=False)
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    mysql_engine = "InnoDB"

