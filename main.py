import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class EntryLayout(Widget):
        pass

class MainApp(App):
        def build(self):
                
                # Database Setup
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred)

                db = firestore.client()
                
                # Load Builder
                Builder.load_file('top10.kv')
                return EntryLayout()
        
        def submit(self):
                pass
        def show_records(self):
                pass
    
if __name__ == '__main__':
    MainApp().run()