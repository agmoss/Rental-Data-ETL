import folium
from folium import plugins


class LocationMap:
    """This class contains functionality 
    for adding data elements to a folium map"""

    def __init__(self, name, fmap):
        self.name = name
        self.fmap = fmap

    @staticmethod
    def html_popup(code1, code2, code3, code4):
        """Add custom HTML markers to the folium popup boxes."""

        html1 = """\
        <html>
        <head></head>
        <body>
            <h3>{code1}</h3>
            <p><br>
            <h4>{code2}</h4>
            <h4>{code3}</h4>
            <h4>{code4}</h4>
            </p>
        </body>
        </html>
        """.format(code1=code1, code2=code2, code3=code3, code4=code4)

        return html1

    def add_item(self, df):
        """Add a popup item to the folium map"""

        # mark a row as a folium marker
        for index, row in df.iterrows():
            popup = LocationMap.html_popup(code1=row['something'], code2=row['latitude'], code3=row['longitude'],
                                           code4=row['something'])

            folium.Marker([row['latitude'], row['longitude']]
                          , icon=folium.Icon(color='black')
                          , popup=popup

                          ).add_to(self.fmap)

        return self.fmap

    @staticmethod
    def color_producer(index):
        """Custom shader"""
        if index < 0.25:
            return 'green'
        elif 0.25 <= index < 0.75:
            return 'orange'
        else:
            return 'red'

    def status_marks(self, df):
        """Add custom heat markers to a folium map"""

        for index, row in df.iterrows():
            # The radius of the circle grows as crossover increases
            radius = row['crossover'] / 1000

            folium.CircleMarker([row['Lat'], row['Lon']]
                                , radius=radius
                                , fill=True
                                , color=self.color_producer(row['Cross_Normal'])
                                , opacity=row['Cross_Normal']

                                , fill_color=self.color_producer(row['Cross_Normal'])
                                , fill_opacity=row['Cross_Normal']

                                # The current popup takes forever to render...
                                # ,popup=popup

                                ).add_to(self.fmap)

        return self.fmap

    def add_heat(self, df):
        """Add standard folium heatmap to the map object."""

        # convert to (n, 2) nd-array format for heat map
        location_arr = df[['latitude', 'longitude']].values

        hm = plugins.HeatMap(location_arr, radius=3, blur=1)
        hm.add_to(self.fmap)