from app.core.user_roles import UserRoles
from app.db.session import Base
from sqlalchemy import Column, Integer, String, Boolean, Enum  # , ForeignKey

# from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True, default="")
    last_name = Column(String, nullable=False)
    role = Column(Enum(UserRoles), nullable=False, default=UserRoles.TEACHER)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # school_id = Column(ForeignKey("schools.id", ondelete="CASCADE"))
    # school = relationship("School", back_populates="users")
