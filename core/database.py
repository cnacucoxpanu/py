from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime 
import enum

from config import config

Base = declarative_base()

class Priority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS_ = "in progress"
    COMPLETED = "completed"

class Task(Base):
    __tablename__ = 'tasks'
    