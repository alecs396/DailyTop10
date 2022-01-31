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
        r0 = ObjectProperty(None)
        r1 = ObjectProperty(None)
        r2 = ObjectProperty(None)
        r3 = ObjectProperty(None)
        r4 = ObjectProperty(None)
        r5 = ObjectProperty(None)
        r6 = ObjectProperty(None)
        r7 = ObjectProperty(None)
        r8 = ObjectProperty(None)
        r9 = ObjectProperty(None)
        
        def submit(self):
                date = self.date.text
                r0 = self.r0.text
                r1 = self.r1.text
                r2 = self.r2.text
                r3 = self.r3.text
                r4 = self.r4.text
                r5 = self.r5.text
                r6 = self.r6.text
                r7 = self.r7.text
                r8 = self.r8.text
                r9 = self.r9.text
        
                data = {"0" : r0,
                        "1" : r1,
                        "2" : r2,
                        "3" : r3,
                        "4" : r4,
                        "5" : r5,
                        "6" : r6,
                        "7" : r7,
                        "8" : r8,
                        "9" : r9}
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