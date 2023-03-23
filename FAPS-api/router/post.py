import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends

import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()

