# 🟩 מקטע 1 – הגדרות בסיס וייבוא ספריות

import os
import random
import datetime
import time
import threading
from flask import Flask
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# יצירת אפליקציה בסיסית לענן Render
app = Flask(__name__)
