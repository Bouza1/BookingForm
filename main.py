import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
import sqlite3
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.clearcolor ="#1C2541" 
Window.size = (470, 800)

db = sqlite3.connect('database.db')
cur = db.cursor()

rose = "#B26E63ff"
turq = "#80FFECff"
fadedBlue = "#779CABff"
duckGrey = "#D5DFE5ff"

global date
date = datetime.datetime.now()

global day
day0Day = date.strftime("%A")
day = day0Day

day0Date = date.strftime("%x")

global dayFormatted
day0Formatted =  day0Day + ' ' + day0Date
dayFormatted = day0Formatted

print(dayFormatted)

global username
username = int(0)

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginBtn(self):
        username1 = self.username.text
        global username
        username = int(username1)
        usernameStr = str(username)
        password1 = self.password.text
        cur.execute(" SELECT COUNT (*) FROM users WHERE username = '"+ usernameStr +"' AND password = '"+ password1 +"' ")
        worked = str(cur.fetchone())
        workedStriped = worked.strip("(").strip(")").strip(",")
        print(workedStriped) 
        print(username)  
        if workedStriped == "1":
            sm.current = "dayScreen"
            self.manager.get_screen('dayScreen').dayLbl = dayFormatted
            print(type(username))
        # add a checker so that as soon as login, day and check is done
        else:
            WrongPasswordPopup().open() 
        
class dayScreen(Screen):
    dayLbl = StringProperty('')

    def forwardDate(self):
        global date
        nextDate = (date + datetime.timedelta(days=1))
        date = nextDate
        nextDay = nextDate.strftime("%A")
        day = nextDay
        nextFullDate = nextDate.strftime("%x")
        nextDayFormatted =  day + ' ' + nextFullDate    
        global dayFormatted
        dayFormatted = nextDayFormatted
        print(dayFormatted)
        self.manager.get_screen('dayScreen').dayLbl = dayFormatted
        today = datetime.datetime.now()
        todayFullDate = today.strftime("%x")
        #block off going backwords in time
        if nextFullDate >= todayFullDate:
            self.ids.backwardButton.disabled = False
        #block off going past 14 days
        twoWeeksTime = today + datetime.timedelta(days=13)
        twoWeeksTimeFullDate = twoWeeksTime.strftime("%x")
        print(twoWeeksTimeFullDate)
        if nextFullDate >= twoWeeksTimeFullDate:
            self.ids.forwardButton.disabled = True
        elif nextFullDate <= twoWeeksTimeFullDate:
            self.ids.forwardButton.disabled = False
        #check db for booking.
        cur.execute("SELECT * FROM twoWeek where date = '"+ dayFormatted +"' ")
        timesBooked = cur.fetchone()
        print(timesBooked)
        print(username)
        print(type(username))
        #if booked
        #7am
        if timesBooked[1] == username:
            self.ids.sevenAM.disabled = True
            self.ids.sevenAM.text = "Booked"
            self.ids.sevenAM.background_color = rose
            self.ids.sevenAMCancel.disabled = False
            self.ids.sevenAMLbl.color = "green"
        elif timesBooked[1] == 0:
            self.ids.sevenAM.disabled = False
            self.ids.sevenAM.text = "Available"
            self.ids.sevenAM.background_color = fadedBlue
            self.ids.sevenAMCancel.disabled = True
            self.ids.sevenAMCancel.disabled = True
            self.ids.sevenAMLbl.color = "white"
        elif timesBooked[1] != username or timesBooked[1] != 0:
            self.ids.sevenAMLbl.color = "#123456"
            self.ids.sevenAM.disabled = True
            self.ids.sevenAM.text = "Not Available"
            self.ids.sevenAM.background_color = rose
            self.ids.sevenAMCancel.disabled = True
        #8am
        if timesBooked[2] == username:
            self.ids.eigthAM.disabled = True
            self.ids.eigthAM.text = "Booked"
            self.ids.eigthAM.background_color = rose
            self.ids.eigthAMCancel.disabled = False
            self.ids.eigthAMLbl.color = "green"
        elif timesBooked[2] == 0:
            self.ids.eigthAM.disabled = False
            self.ids.eigthAM.text = "Available"
            self.ids.eigthAM.background_color = fadedBlue
            self.ids.eigthAMCancel.disabled = True
            self.ids.eigthAMLbl.color = "white"
        elif timesBooked[2] != username or timesBooked[2] != 0:
            self.ids.eigthAM.disabled = True
            self.ids.eigthAM.text = "Not Available"
            self.ids.eigthAM.background_color = rose
            self.ids.eigthAMCancel.disabled = True
            self.ids.eigthAMLbl.color = "#123456"
        #9am
        if timesBooked[3] == username:
            self.ids.nineAM.disabled = True
            self.ids.nineAM.text = "Booked"
            self.ids.nineAM.background_color = rose
            self.ids.nineAMCancel.disabled = False
            self.ids.nineAMLbl.color = "green"
        elif timesBooked[3] == 0:
            self.ids.nineAM.disabled = False
            self.ids.nineAM.text = "Available"
            self.ids.nineAM.background_color = fadedBlue
            self.ids.nineAMCancel.disabled = True
            self.ids.nineAMLbl.color = "white"
        elif timesBooked[3] != username or timesBooked[3] != 0:
            self.ids.nineAM.disabled = True
            self.ids.nineAM.text = "Not Available"
            self.ids.nineAM.background_color = rose
            self.ids.nineAMCancel.disabled = True
            self.ids.nineAMLbl.color = "#123456"
        #10am
        if timesBooked[4] == username:
            self.ids.tenAM.disabled = True
            self.ids.tenAM.text = "Booked"
            self.ids.tenAM.background_color = rose
            self.ids.tenAMCancel.disabled = False
            self.ids.tenAMLbl.color = "green"
        elif timesBooked[4] == 0:
            self.ids.tenAM.disabled = False
            self.ids.tenAM.text = "Available"
            self.ids.tenAM.background_color = fadedBlue
            self.ids.tenAMCancel.disabled = True
            self.ids.tenAMLbl.color = "white"
        elif timesBooked[4] != username or timesBooked[4] != 0:
            self.ids.tenAM.disabled = True
            self.ids.tenAM.text = "Not Available"
            self.ids.tenAM.background_color = rose
            self.ids.tenAMCancel.disabled = True
            self.ids.tenAMLbl.color = "#123456"
        #11am
        if timesBooked[5] == username:
            self.ids.elevenAM.disabled = True
            self.ids.elevenAM.text = "Booked"
            self.ids.elevenAM.background_color = rose
            self.ids.elevenAMCancel.disabled = False
            self.ids.elevenAMLbl.color = "green"
        elif timesBooked[5] == 0:
            self.ids.elevenAM.disabled = False
            self.ids.elevenAM.text = "Available"
            self.ids.elevenAM.background_color = fadedBlue
            self.ids.elevenAMCancel.disabled = True
            self.ids.elevenAMLbl.color = "white"
        elif timesBooked[5] != username or timesBooked[5] != 0:
            self.ids.elevenAM.disabled = True
            self.ids.elevenAM.text = "Not Available"
            self.ids.elevenAM.background_color = rose
            self.ids.elevenAMCancel.disabled = True
            self.ids.elevenAMLbl.color = "#123456"
        #12pm
        if timesBooked[6] == username:
            self.ids.twelvePM.disabled = True
            self.ids.twelvePM.text = "Booked"
            self.ids.twelvePM.background_color = rose
            self.ids.twelvePMCancel.disabled = False
            self.ids.twelvePMlbl.color = "green"
        elif timesBooked[6] == 0:
            self.ids.twelvePM.disabled = False
            self.ids.twelvePM.text = "Available"
            self.ids.twelvePM.background_color = fadedBlue
            self.ids.twelvePMCancel.disabled = True
            self.ids.twelvePMlbl.color = "white"
        elif timesBooked[6] != username or timesBooked[6] != 0:
            self.ids.twelvePM.disabled = True
            self.ids.twelvePM.text = "Not Available"
            self.ids.twelvePM.background_color = rose
            self.ids.twelvePMCancel.disabled = True
            self.ids.twelvePMlbl.color = "#123456"
        #1pm
        if timesBooked[7] == username:
            self.ids.onePM.disabled = True
            self.ids.onePM.text = "Booked"
            self.ids.onePM.background_color = rose
            self.ids.onePMCancel.disabled = False
            self.ids.onePMLbl.color = "green"
        elif timesBooked[7] == 0:
            self.ids.onePM.disabled = False
            self.ids.onePM.text = "Available"
            self.ids.onePM.background_color = fadedBlue
            self.ids.onePMCancel.disabled = True
            self.ids.onePMLbl.color = "white"
        elif timesBooked[7] != username or timesBooked[7] != 0:
            self.ids.onePM.disabled = True
            self.ids.onePM.text = "Not Available"
            self.ids.onePM.background_color = rose
            self.ids.onePMCancel.disabled = True
            self.ids.onePMLbl.color = "#123456"
        #2pm
        if timesBooked[8] == username:
            self.ids.twoPM.disabled = True
            self.ids.twoPM.text = "Booked"
            self.ids.twoPM.background_color = rose
            self.ids.twoPMCancel.disabled = False
            self.ids.twoPMLbl.color = "green"
        elif timesBooked[8] == 0:
            self.ids.twoPM.disabled = False
            self.ids.twoPM.text = "Available"
            self.ids.twoPM.background_color = fadedBlue
            self.ids.twoPMCancel.disabled = True
            self.ids.twoPMLbl.color = "white"
        elif timesBooked[8] != username or timesBooked[8] != 0:
            self.ids.twoPM.disabled = True
            self.ids.twoPM.text = "Not Available"
            self.ids.twoPM.background_color = rose
            self.ids.twoPMCancel.disabled = True
            self.ids.twoPMLbl.color = "#123456"
        #3pm
        if timesBooked[9] == username:
            self.ids.threePM.disabled = True
            self.ids.threePM.text = "Booked"
            self.ids.threePM.background_color = rose
            self.ids.threePMCancel.disabled = False
            self.ids.threePMLbl.color = "green"
        elif timesBooked[9] == 0:
            self.ids.threePM.disabled = False
            self.ids.threePM.text = "Available"
            self.ids.threePM.background_color = fadedBlue
            self.ids.threePMCancel.disabled = True
            self.ids.threePMLbl.color = "white"
        elif timesBooked[9] != username or timesBooked[9] != 0:
            self.ids.threePM.disabled = True
            self.ids.threePM.text = "Not Available"
            self.ids.threePM.background_color = rose
            self.ids.threePMCancel.disabled = True
            self.ids.threePMLbl.color = "#123456"
        #4pm
        if timesBooked[10] == username:
            self.ids.fourPM.disabled = True
            self.ids.fourPM.text = "Booked"
            self.ids.fourPM.background_color = rose
            self.ids.fourPMCancel.disabled = False
            self.ids.fourPMLbl.color = "green"
        elif timesBooked[10] == 0:
            self.ids.fourPM.disabled = False
            self.ids.fourPM.text = "Available"
            self.ids.fourPM.background_color = fadedBlue
            self.ids.fourPMCancel.disabled = True
            self.ids.fourPMLbl.color = "white"
        elif timesBooked[10] != username or timesBooked[10] != 0:
            self.ids.fourPM.disabled = True
            self.ids.fourPM.text = "Not Available"
            self.ids.fourPM.background_color = rose
            self.ids.fourPMCancel.disabled = True
            self.ids.fourPMLbl.color = "#123456"
        #5pm
        if timesBooked[11] == username:
            self.ids.fivePM.disabled = True
            self.ids.fivePM.text = "Booked"
            self.ids.fivePM.background_color = rose
            self.ids.fivePMCancel.disabled = False
            self.ids.fivePMLbl.color = "green"
        elif timesBooked[11] == 0:
            self.ids.fivePM.disabled = False
            self.ids.fivePM.text = "Available"
            self.ids.fivePM.background_color = fadedBlue
            self.ids.fivePMCancel.disabled = True
            self.ids.fivePMLbl.color = "white"
        elif timesBooked[11] != username or timesBooked[11] != 0:
            self.ids.fivePM.disabled = True
            self.ids.fivePM.text = "Not Available"
            self.ids.fivePM.background_color = rose
            self.ids.fivePMCancel.disabled = True
            self.ids.fivePMLbl.color = "#123456"
        #6pm
        if timesBooked[12] == username:
            self.ids.sixPM.disabled = True
            self.ids.sixPM.text = "Booked"
            self.ids.sixPM.background_color = rose
            self.ids.sixPMCancel.disabled = False
            self.ids.sixPMLbl.color = "green"
        elif timesBooked[12] == 0:
            self.ids.sixPM.disabled = False
            self.ids.sixPM.text = "Available"
            self.ids.sixPM.background_color = fadedBlue
            self.ids.sixPMCancel.disabled = True
            self.ids.sixPMLbl.color = "white"
        elif timesBooked[12] != username or timesBooked[12] != 0:
            self.ids.sixPM.disabled = True
            self.ids.sixPM.text = "Not Available"
            self.ids.sixPM.background_color = rose
            self.ids.sixPMCancel.disabled = True
            self.ids.sixPMLbl.color = "#123456"
        #7pm
        if timesBooked[13] == username:
            self.ids.sevenPM.disabled = True
            self.ids.sevenPM.text = "Booked"
            self.ids.sevenPM.background_color = rose
            self.ids.sevenPMCancel.disabled = False
            self.ids.sevenPMLbl.color = "green"
        elif timesBooked[13] == 0:
            self.ids.sevenPM.disabled = False
            self.ids.sevenPM.text = "Available"
            self.ids.sevenPM.background_color = fadedBlue
            self.ids.sevenPMCancel.disabled = True
            self.ids.sevenPMLbl.color = "white"
        elif timesBooked[13] != username or timesBooked[13] != 0:
            self.ids.sevenPM.disabled = True
            self.ids.sevenPM.text = "Not Available"
            self.ids.sevenPM.background_color = rose
            self.ids.sevenPMCancel.disabled = True
            self.ids.sevenPMLbl.color = "#123456"

    def backwardDate(self):
        global date
        backDate = (date - datetime.timedelta(days=1))
        date = backDate
        backDay = backDate.strftime("%A")
        day = backDay
        backFullDate = backDate.strftime("%x")
        backDayFormatted =  day + ' ' + backFullDate    
        global dayFormatted
        dayFormatted = backDayFormatted
        self.manager.get_screen('dayScreen').dayLbl = dayFormatted        
        #print(dayFormatted)
        today = datetime.datetime.now()
        todayFullDate = today.strftime("%x")
        print(backFullDate)
        print(todayFullDate)
        if backFullDate <= todayFullDate:
            self.ids.backwardButton.disabled = True

        twoWeeksTime = today + datetime.timedelta(days=13)
        twoWeeksTimeFullDate = twoWeeksTime.strftime("%x")
        print(twoWeeksTimeFullDate)
        #block off going past 14 days
        if backFullDate <= twoWeeksTimeFullDate:
            self.ids.forwardButton.disabled = False
        #check for bookings
        cur.execute("SELECT * FROM twoWeek where date = '"+ dayFormatted +"' ")
        timesBooked = cur.fetchone()
        print(timesBooked)
        #if booked
        #7am
        if timesBooked[1] == username:
            self.ids.sevenAM.disabled = True
            self.ids.sevenAM.text = "Booked"
            self.ids.sevenAM.background_color = rose
            self.ids.sevenAMCancel.disabled = False
        elif timesBooked[1] == 0:
            self.ids.sevenAM.disabled = False
            self.ids.sevenAM.text = "Available"
            self.ids.sevenAM.background_color = fadedBlue
            self.ids.sevenAMCancel.disabled = True
            self.ids.sevenAMCancel.disabled = True
        elif timesBooked[1] != username or timesBooked[1] != 0:
            self.ids.sevenAM.disabled = True
            self.ids.sevenAM.text = "Not Available"
            self.ids.sevenAM.background_color = rose
            self.ids.sevenAMCancel.disabled = True
        #8am
        if timesBooked[2] == username:
            self.ids.eigthAM.disabled = True
            self.ids.eigthAM.text = "Booked"
            self.ids.eigthAM.background_color = rose
            self.ids.eigthAMCancel.disabled = False
        elif timesBooked[2] == 0:
            self.ids.eigthAM.disabled = False
            self.ids.eigthAM.text = "Available"
            self.ids.eigthAM.background_color = fadedBlue
            self.ids.eigthAMCancel.disabled = True
        elif timesBooked[2] != username or timesBooked[2] != 0:
            self.ids.eigthAM.disabled = True
            self.ids.eigthAM.text = "Not Available"
            self.ids.eigthAM.background_color = rose
            self.ids.eigthAMCancel.disabled = True
        #9am
        if timesBooked[3] == username:
            self.ids.nineAM.disabled = True
            self.ids.nineAM.text = "Booked"
            self.ids.nineAM.background_color = rose
            self.ids.nineAMCancel.disabled = False
        elif timesBooked[3] == 0:
            self.ids.nineAM.disabled = False
            self.ids.nineAM.text = "Available"
            self.ids.nineAM.background_color = fadedBlue
            self.ids.nineAMCancel.disabled = True
        elif timesBooked[3] != username or timesBooked[3] != 0:
            self.ids.nineAM.disabled = True
            self.ids.nineAM.text = "Not Available"
            self.ids.nineAM.background_color = rose
            self.ids.nineAMCancel.disabled = True
        #10am
        if timesBooked[4] == username:
            self.ids.tenAM.disabled = True
            self.ids.tenAM.text = "Booked"
            self.ids.tenAM.background_color = rose
            self.ids.tenAMCancel.disabled = False
        elif timesBooked[4] == 0:
            self.ids.tenAM.disabled = False
            self.ids.tenAM.text = "Available"
            self.ids.tenAM.background_color = fadedBlue
            self.ids.tenAMCancel.disabled = True
            self.ids.tenAMCancel.disabled = True
        elif timesBooked[4] != username or timesBooked[4] != 0:
            self.ids.tenAM.disabled = True
            self.ids.tenAM.text = "Not Available"
            self.ids.tenAM.background_color = rose
            self.ids.tenAMCancel.disabled = True
        #11am
        if timesBooked[5] == username:
            self.ids.elevenAM.disabled = True
            self.ids.elevenAM.text = "Booked"
            self.ids.elevenAM.background_color = rose
            self.ids.elevenAMCancel.disabled = False
        elif timesBooked[5] == 0:
            self.ids.elevenAM.disabled = False
            self.ids.elevenAM.text = "Available"
            self.ids.elevenAM.background_color = fadedBlue
            self.ids.elevenAMCancel.disabled = True
            self.ids.elevenAMCancel.disabled = True
        elif timesBooked[5] != username or timesBooked[5] != 0:
            self.ids.elevenAM.disabled = True
            self.ids.elevenAM.text = "Not Available"
            self.ids.elevenAM.background_color = rose
            self.ids.elevenAMCancel.disabled = True
        #12pm
        if timesBooked[6] == username:
            self.ids.twelvePM.disabled = True
            self.ids.twelvePM.text = "Booked"
            self.ids.twelvePM.background_color = rose
            self.ids.twelvePMCancel.disabled = False
        elif timesBooked[6] == 0:
            self.ids.twelvePM.disabled = False
            self.ids.twelvePM.text = "Available"
            self.ids.twelvePM.background_color = fadedBlue
            self.ids.twelvePMCancel.disabled = True
            self.ids.twelvePMCancel.disabled = True
        elif timesBooked[6] != username or timesBooked[6] != 0:
            self.ids.twelvePM.disabled = True
            self.ids.twelvePM.text = "Not Available"
            self.ids.twelvePM.background_color = rose
            self.ids.twelvePMCancel.disabled = True
        #1pm
        if timesBooked[7] == username:
            self.ids.onePM.disabled = True
            self.ids.onePM.text = "Booked"
            self.ids.onePM.background_color = rose
            self.ids.onePMCancel.disabled = False
        elif timesBooked[7] == 0:
            self.ids.onePM.disabled = False
            self.ids.onePM.text = "Available"
            self.ids.onePM.background_color = fadedBlue
            self.ids.onePMCancel.disabled = True
        elif timesBooked[7] != username or timesBooked[7] != 0:
            self.ids.onePM.disabled = True
            self.ids.onePM.text = "Not Available"
            self.ids.onePM.background_color = rose
            self.ids.onePMCancel.disabled = True
        #2pm
        if timesBooked[8] == username:
            self.ids.twoPM.disabled = True
            self.ids.twoPM.text = "Booked"
            self.ids.twoPM.background_color = rose
            self.ids.twoPMCancel.disabled = False
        elif timesBooked[8] == 0:
            self.ids.twoPM.disabled = False
            self.ids.twoPM.text = "Available"
            self.ids.twoPM.background_color = fadedBlue
            self.ids.twoPMCancel.disabled = True
            self.ids.twoPMCancel.disabled = True
        elif timesBooked[8] != username or timesBooked[8] != 0:
            self.ids.twoPM.disabled = True
            self.ids.twoPM.text = "Not Available"
            self.ids.twoPM.background_color = rose
            self.ids.twoPMCancel.disabled = True
        #3pm
        if timesBooked[9] == username:
            self.ids.threePM.disabled = True
            self.ids.threePM.text = "Booked"
            self.ids.threePM.background_color = rose
            self.ids.threePMCancel.disabled = False
        elif timesBooked[9] == 0:
            self.ids.threePM.disabled = False
            self.ids.threePM.text = "Available"
            self.ids.threePM.background_color = fadedBlue
            self.ids.threePMCancel.disabled = True
            self.ids.threePMCancel.disabled = True
        elif timesBooked[9] != username or timesBooked[9] != 0:
            self.ids.threePM.disabled = True
            self.ids.threePM.text = "Not Available"
            self.ids.threePM.background_color = rose
            self.ids.threePMCancel.disabled = True
        #4pm
        if timesBooked[10] == username:
            self.ids.fourPM.disabled = True
            self.ids.fourPM.text = "Booked"
            self.ids.fourPM.background_color = rose
            self.ids.fourPMCancel.disabled = False
        elif timesBooked[10] == 0:
            self.ids.fourPM.disabled = False
            self.ids.fourPM.text = "Available"
            self.ids.fourPM.background_color = fadedBlue
            self.ids.fourPMCancel.disabled = True
            self.ids.fourPMCancel.disabled = True
        elif timesBooked[10] != username or timesBooked[10] != 0:
            self.ids.fourPM.disabled = True
            self.ids.fourPM.text = "Not Available"
            self.ids.fourPM.background_color = rose
            self.ids.fourPMCancel.disabled = True
        #5pm
        if timesBooked[11] == username:
            self.ids.fivePM.disabled = True
            self.ids.fivePM.text = "Booked"
            self.ids.fivePM.background_color = rose
            self.ids.fivePMCancel.disabled = False
        elif timesBooked[11] == 0:
            self.ids.fivePM.disabled = False
            self.ids.fivePM.text = "Available"
            self.ids.fivePM.background_color = fadedBlue
            self.ids.fivePMCancel.disabled = True
            self.ids.fivePMCancel.disabled = True
        elif timesBooked[11] != username or timesBooked[11] != 0:
            self.ids.fivePM.disabled = True
            self.ids.fivePM.text = "Not Available"
            self.ids.fivePM.background_color = rose
            self.ids.fivePMCancel.disabled = True
        #6pm
        if timesBooked[12] == username:
            self.ids.sixPM.disabled = True
            self.ids.sixPM.text = "Booked"
            self.ids.sixPM.background_color = rose
            self.ids.sixPMCancel.disabled = False
        elif timesBooked[12] == 0:
            self.ids.sixPM.disabled = False
            self.ids.sixPM.text = "Available"
            self.ids.sixPM.background_color = fadedBlue
            self.ids.sixPMCancel.disabled = True
            self.ids.sixPMCancel.disabled = True
        elif timesBooked[12] != username or timesBooked[12] != 0:
            self.ids.sixPM.disabled = True
            self.ids.sixPM.text = "Not Available"
            self.ids.sixPM.background_color = rose
            self.ids.sixPMCancel.disabled = True
        #7pm
        if timesBooked[13] == username:
            self.ids.sevenPM.disabled = True
            self.ids.sevenPM.text = "Booked"
            self.ids.sevenPM.background_color = rose
            self.ids.sevenPMCancel.disabled = False
        elif timesBooked[13] == 0:
            self.ids.sevenPM.disabled = False
            self.ids.sevenPM.text = "Available"
            self.ids.sevenPM.background_color = fadedBlue
            self.ids.sevenPMCancel.disabled = True
            self.ids.sevenPMCancel.disabled = True
        elif timesBooked[13] != username or timesBooked[13] != 0:
            self.ids.sevenPM.disabled = True
            self.ids.sevenPM.text = "Not Available"
            self.ids.sevenPM.background_color = rose
            self.ids.sevenPMCancel.disabled = True

    def book7am(self):
        usernameStr = str(username)
        self.ids.sevenAM.disabled = True
        self.ids.sevenAM.text = "Booked"
        self.ids.sevenAM.background_normal = ""
        self.ids.sevenAM.background_color = rose
        self.ids.sevenAMCancel.disabled = False
        self.ids.sevenAMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET seven = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book8am(self):
        usernameStr = str(username)
        self.ids.eigthAM.disabled = True
        self.ids.eigthAM.text = "Booked"
        self.ids.eigthAM.background_color = rose
        self.ids.eigthAMCancel.disabled = False
        self.ids.eigthAMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET eigth = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book9am(self):
        usernameStr = str(username)
        self.ids.nineAM.disabled = True
        self.ids.nineAM.text = "Booked"
        self.ids.nineAM.background_color = rose
        self.ids.nineAMCancel.disabled = False
        self.ids.nineAMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET nine = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book10am(self):
        usernameStr = str(username)
        self.ids.tenAM.disabled = True
        self.ids.tenAM.text = "Booked"
        self.ids.tenAM.background_color = rose
        self.ids.tenAMCancel.disabled = False
        self.ids.tenAMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET ten = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book11am(self):
        usernameStr = str(username)
        self.ids.elevenAM.disabled = True
        self.ids.elevenAM.text = "Booked"
        self.ids.elevenAM.background_color = rose
        self.ids.elevenAMCancel.disabled = False
        self.ids.elevenAMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET eleven = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book12pm(self):
        usernameStr = str(username)
        self.ids.twelvePM.disabled = True
        self.ids.twelvePM.text = "Booked"
        self.ids.twelvePM.background_color = rose
        self.ids.twelvePMCancel.disabled = False
        self.ids.twelvePMlbl.color = "green"
        cur.execute("UPDATE twoWeek SET twelve = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book1pm(self):
        usernameStr = str(username)
        self.ids.onePM.disabled = True
        self.ids.onePM.text = "Booked"
        self.ids.onePM.background_color = rose
        self.ids.onePMCancel.disabled = False
        self.ids.onePMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET thirteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book2pm(self):
        usernameStr = str(username)
        self.ids.twoPM.disabled = True
        self.ids.twoPM.text = "Booked"
        self.ids.twoPM.background_color = rose
        self.ids.twoPMCancel.disabled = False
        self.ids.twoPMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET fourteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book3pm(self):
        usernameStr = str(username)
        self.ids.threePM.disabled = True
        self.ids.threePM.text = "Booked"
        self.ids.threePM.background_color = rose
        self.ids.threePMCancel.disabled = False
        self.ids.threePMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET fifteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book4pm(self):
        usernameStr = str(username)
        self.ids.fourPM.disabled = True
        self.ids.fourPM.text = "Booked"
        self.ids.fourPM.background_color = rose
        self.ids.fourPMCancel.disabled = False
        self.ids.fourPMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET sixteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book5pm(self):
        usernameStr = str(username)
        self.ids.fivePM.disabled = True
        self.ids.fivePM.text = "Booked"
        self.ids.fivePM.background_color = rose
        self.ids.fivePMCancel.disabled = False
        self.ids.fivePMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET seventeen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book6pm(self):
        usernameStr = str(username)
        self.ids.sixPM.disabled = True
        self.ids.sixPM.text = "Booked"
        self.ids.sixPM.background_color = rose
        self.ids.sixPMCancel.disabled = False
        self.ids.sixPMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET eigthteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def book7pm(self):
        usernameStr = str(username)
        self.ids.sevenPM.disabled = True
        self.ids.sevenPM.text = "Booked"
        self.ids.sevenPM.background_color = rose
        self.ids.sevenPMCancel.disabled = False
        self.ids.sevenPMLbl.color = "green"
        cur.execute("UPDATE twoWeek SET nineteen = '"+ usernameStr +"' WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel7am(self):
        self.ids.sevenAM.disabled = False
        self.ids.sevenAM.text = "Available"
        self.ids.sevenAM.background_normal = ""
        self.ids.sevenAM.background_color = fadedBlue
        self.ids.sevenAMCancel.disabled = True
        self.ids.sevenAMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET seven = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel8am(self):
        self.ids.eigthAM.disabled = False
        self.ids.eigthAM.text = "Available"
        self.ids.eigthAM.background_normal = ""
        self.ids.eigthAM.background_color = fadedBlue
        self.ids.eigthAMCancel.disabled = True
        self.ids.eigthAMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET eigth = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel9am(self):
        self.ids.nineAM.disabled = False
        self.ids.nineAM.text = "Available"
        self.ids.nineAM.background_normal = ""
        self.ids.nineAM.background_color = fadedBlue
        self.ids.nineAMCancel.disabled = True
        self.ids.nineAMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET nine = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel10am(self):
        self.ids.tenAM.disabled = False
        self.ids.tenAM.text = "Available"
        self.ids.tenAM.background_normal = ""
        self.ids.tenAM.background_color = fadedBlue
        self.ids.tenAMCancel.disabled = True
        self.ids.tenAMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET ten = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel11am(self):
        self.ids.elevenAM.disabled = False
        self.ids.elevenAM.text = "Available"
        self.ids.elevenAM.background_normal = ""
        self.ids.elevenAM.background_color = fadedBlue
        self.ids.elevenAMCancel.disabled = True
        self.ids.elevenAMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET eleven = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel12pm(self):
        self.ids.twelvePM.disabled = False
        self.ids.twelvePM.text = "Available"
        self.ids.twelvePM.background_normal = ""
        self.ids.twelvePM.background_color = fadedBlue
        self.ids.twelvePMCancel.disabled = True
        self.ids.twelvePMlbl.color = "white"
        cur.execute("UPDATE twoWeek SET twelve = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel1pm(self):
        self.ids.onePM.disabled = False
        self.ids.onePM.text = "Available"
        self.ids.onePM.background_normal = ""
        self.ids.onePM.background_color = fadedBlue
        self.ids.onePMCancel.disabled = True
        self.ids.onePMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET thirteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel2pm(self):
        self.ids.twoPM.disabled = False
        self.ids.twoPM.text = "Available"
        self.ids.twoPM.background_normal = ""
        self.ids.twoPM.background_color = fadedBlue
        self.ids.twoPMCancel.disabled = True
        self.ids.twoPMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET fourteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel3pm(self):
        self.ids.threePM.disabled = False
        self.ids.threePM.text = "Available"
        self.ids.threePM.background_normal = ""
        self.ids.threePM.background_color = fadedBlue
        self.ids.threePMCancel.disabled = True
        self.ids.threePMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET fifteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel4pm(self):
        self.ids.fourPM.disabled = False
        self.ids.fourPM.text = "Available"
        self.ids.fourPM.background_normal = ""
        self.ids.fourPM.background_color = fadedBlue
        self.ids.fourPMCancel.disabled = True
        self.ids.fourPMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET sixteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel5pm(self):
        self.ids.fivePM.disabled = False
        self.ids.fivePM.text = "Available"
        self.ids.fivePM.background_normal = ""
        self.ids.fivePM.background_color = fadedBlue
        self.ids.fivePMCancel.disabled = True
        self.ids.fivePMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET seventeen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel6pm(self):
        self.ids.sixPM.disabled = False
        self.ids.sixPM.text = "Available"
        self.ids.sixPM.background_normal = ""
        self.ids.sixPM.background_color = fadedBlue
        self.ids.sixPMCancel.disabled = True
        self.ids.sixPMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET eigthteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancel7pm(self):
        self.ids.sevenPM.disabled = False
        self.ids.sevenPM.text = "Available"
        self.ids.sevenPM.background_normal = ""
        self.ids.sevenPM.background_color = fadedBlue
        self.ids.sevenPMCancel.disabled = True
        self.ids.sevenPMLbl.color = "white"
        cur.execute("UPDATE twoWeek SET nineteen = 0 WHERE date = '"+ dayFormatted +"' ")
        db.commit()

    def cancelScr(self):
        sm.current = 'cancelScreen'

class cancelScreen(Screen):
    pass

class WrongPasswordPopup(Popup):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

sm = WindowManager()
sm.add_widget(LoginScreen(name='loginScreen'))
sm.add_widget(dayScreen(name='dayScreen'))
sm.add_widget(cancelScreen(name='Screen'))

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
