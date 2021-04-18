import mysql.connector
import threading
import keyboard
from exit_thread import my_monitoring
from program import my_thread
from method1 import *
from method2 import *
from method3 import *
from method4 import *
from method5 import *

db_connection = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="Timetable"
)

db_cursor = db_connection.cursor()

my_monitoring.start()
my_thread.start()