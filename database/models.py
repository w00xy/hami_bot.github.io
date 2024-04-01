from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    referer_id: Mapped[str] = mapped_column(String(15), nullable=True, default=None)
    balance: Mapped[str] = mapped_column(String(15), nullable=True, default=0)
    reposted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
