import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
    
# Database Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
class EntryLayout(Screen):
        """This class is the Entry page.  It builds off of the top10.kv file."""
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
                """This function will submit an entry to the database."""
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
                # Send to database
                db.collection("top 10").document(date).set(data)

                # Create Message
                self.ids.top_label.text = "Entry Submitted!"
                
                # Clear Entry Boxes
                self.ids.date.text = ''
                self.ids.r0.text = ''
                self.ids.r1.text = ''
                self.ids.r2.text = ''
                self.ids.r3.text = ''
                self.ids.r4.text = ''
                self.ids.r5.text = ''
                self.ids.r6.text = ''
                self.ids.r7.text = ''
                self.ids.r8.text = ''
                self.ids.r9.text = ''
class ViewerScreen(Screen):
        date = ObjectProperty(None)
        
        def show_records(self):
                date = self.date.text
                
                # Pull from database
                records = db.collection("top 10").document(date).get()
                 
                if records.exists:
                        result = records.to_dict()
                        print(result)
                        
                        # Display Records
                        # self.ids.record.text = text
                else:
                        print('DATE DOES NOT EXIST')
                        # self.ids.record.text = "ENTRY DOES NOT EXIST"
                
                
                       
               
class WindowManager(ScreenManager):
        pass

class MainApp(App):
        def build(self):
                # Load Builder
                kv = Builder.load_file('top10.kv')
                return kv
        

    
if __name__ == '__main__':
    MainApp().run()