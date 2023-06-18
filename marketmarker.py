from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class MarketMarker(MapMarkerPopup):
    print("  sono in line 6 di MarketMarker")
    #source = "marker.png"
    market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()

