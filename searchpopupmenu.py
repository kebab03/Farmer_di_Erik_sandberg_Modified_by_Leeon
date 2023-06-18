from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
from kivy.clock import Clock
 
class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'
 
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback
 
    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)
 
    def callback(self, *args):
        address = self.text_field.text
        print("address")
        print(address)
        self.geocode_get_lat_lon(address)
 
    def geocode_get_lat_lon(self, address):
       
        address = parse.quote(address)
 
        akpin ="g9urwnb1HU_0fRT_0vJdSNKN1mVcF0qsiqCadrwIiUE"
 
        url = f"https://geocode.search.hereapi.com/v1/geocode?q={address}&limit=4&apiKey={akpin}"
        #url = "https://geocode.search.hereapi.com/v1/geocode?q=Napoli&limit=4&apiKey=g9urwnb1HU_0fRT_0vJdSNKN1mVcF0qsiqCadrwIiUE" 
        #url = "https://revgeocode.search.hereapi.com/v1/revgeocode?at=48.2181679%2C16.3899064&lang=en-US&apiKey=g9urwnb1HU_0fRT_0vJdSNKN1mVcF0qsiqCadrwIiUE"
        #url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        #U11.47 min   Urlrequest è un Get asincronous
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())
 
    def success(self, urlrequest, result):
        print("Success")
        print(result)
        print("---------------------------------------------------result--------------------------------------------")
        print(result['items'])
        print("---------------------------------------------------result[1]['position']--------------------------------------------")
      
        print(result['items'][0]['position'])# 0 per Usa , 1 Per EUropa
        #latitude = result['items'][1]['position']['lat']
        latitude = result['items'][0]['position']['lat']
        print("*****************************************latitude***************************")
        print(latitude)
        #longitude = result['items'][1]['position']['lng']# 0 per Usa , 1 Per EUropa
        longitude = result['items'][0]['position']['lng']
        print("*****************************************longitude***************************")
        print(longitude)
        """
        questi sono vechi
        #latitude = result['items']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        #longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        """
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude) 
 
    def error(self, urlrequest, result):
        print("error")
        print(result)
 
    def failure(self, urlrequest, result):
        print("failure")
        print(result)
