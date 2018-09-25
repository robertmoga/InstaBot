import time
from multiprocessing import Process
from services import get_users as gu
import sqlite3
from utils import date_time_manager as dtm

print(dtm.get_next_time(False, False))
