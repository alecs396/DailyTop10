import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
             
# Database Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class EntryLayout(Widget):
        date = ObjectProperty(None)
        r1 = ObjectProperty(None)
        def submit(self):
                date = self.date.text
                r1 = self.r1.text
                data = {"1" : r1}
                db.collection("top 10").document(date).set(data)

class MainApp(App):
        def build(self):
                # Load Builder
                Builder.load_file('top10.kv')
                return EntryLayout()
        
        def show_records(self):
                pass
    
if __name__ == '__main__':
    MainApp().run()