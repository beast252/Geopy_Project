import folium,pandas
data=pandas.read_excel(r"practice\MAP with Marker\Airports.xlsx",sheet_name=0)
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["name"])
elev=list(data["ELE"])
def gc(e=None):
    if e>2000:
        return "orange"
    elif 1000<e<=2000:
        return "Yellow"
    else:
        return "blue"
html="""
Airport Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""
map=folium.Map(location=[24.24,77.57],zoom_start=6,tiles="Stamen Terrain")

fgp=folium.FeatureGroup(name="World Population")
fgp.add_child(folium.GeoJson(data=open(r'C:\Users\shahb\OneDrive\Documents\Python\practice\MAP with Marker\world.json',
'r',encoding='utf-8-sig').read(),style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<50000000
else 'orange' if 50000000<=x['properties']['POP2005']<100000000 else'red'}))

fg=folium.FeatureGroup(name="India Airports")
for lt,ln,el,n in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (n,n), width=150, height=90)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6 ,popup=folium.Popup(iframe),
    fill_color=gc(el),color='black',fill=True,fill_opacity=0.86))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("AirportMAP.html")