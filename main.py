import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import kivy
from kivy.app import App
from kivy.uix.label import Label

# Database Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

"""
# Test setup
data = {"1) " : "Sam is Happy",
        "2) " : "I have my degree"}
db.collection("top 10").document("10-16-2022").set(data)
"""
