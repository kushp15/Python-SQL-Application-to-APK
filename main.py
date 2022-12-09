import mysql.connector
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    def abc(self):
        mydb = mysql.connector.Connect(
          # Insert you PC Host Name (IP address)
            host='',
            user='root',
            password='password',
            database='mydatabase'
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM data WHERE asset = 2")

        for X in mycursor:
            self.ids.asset.text = X[3]
        mydb.commit()
        mydb.close()

class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('test.kv')
        return kv

if __name__ == "__main__":
    MyApp().run()
