from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker

class FarmersMapView(MapView):
    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print("g------------------markets---------------------")
        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)
                print("g-----------lin 33-------markets")
                #print( market)

    def add_market(self, market):
        # Create the MarketMarker
        lat, lon = market[21], market[20]
        print("line 39 in farmview")
        print(f"lat := {lat}")

        print(f"lon := {lon}")
        marker = MarketMarker(lat=lat, lon=lon)
        marker.market_data = market
        print(f" marker.market_data :-{marker.market_data}")
        #print(marker.market_data)
        # Add the MarketMarker to the map
        self.add_widget(marker)
        print("chiamto marker")

        # Keep track of the marker's name
        name = market[1]
        self.market_names.append(name)






