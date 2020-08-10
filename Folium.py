#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import folium as fo
import branca


# In[2]:


map=fo.Map(tiles = 'Stamen Terrain', zoom_start=5,control_scale=True)
                    


# In[3]:


x=fo.FeatureGroup(name='my map')


# In[6]:


volcano=pd.read_csv('volcano.csv')


# In[7]:


volcano.head()


# In[8]:


lon_vo=list(volcano['Longitude'])
lat_vo=list(volcano['Longitude'])


# In[25]:


def fancy_html(row):
    i=row
    name_vo=volcano['Name'].iloc[i]
    death_vo=volcano['TOTAL_DEATHS'].iloc[i]
    year_vo=volcano['Year'].iloc[i]
    loc_vo=volcano['Location'].iloc[i]
    country_vo=volcano['Country'].iloc[i]
    
    left_col_colour = "#2A799C"
    right_col_colour = "#C5DCE7"
    
    
    html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:0"; width="25px">{}</h4>""".format(name_vo) + """

</head>
    <table style="height: 126px; width: 300px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Number of Deaths</span></td>
<td style="width: 300px;background-color: """+ right_col_colour +""";">{}</td>""".format(death_vo) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Year</span></td>
<td style="width: 300px;background-color: """+ right_col_colour +""";">{}</td>""".format(year_vo) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Location</span></td>
<td style="width: 300px;background-color: """+ right_col_colour +""";">{}</td>""".format(loc_vo) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Country</span></td>
<td style="width: 300px;background-color: """+ right_col_colour +""";">{}</td>""".format(country_vo) + """
</tr>
</tbody>
</table>
</html>
"""
    return html



# In[10]:


for lat, lon in zip(lat_vo, lon_vo):
    x.add_child(fo.Marker(location=[lat,lon])).add_to(map)


# In[22]:


for i in range(0, len(volcano)):
    html=fancy_html(i)
    
    iframe=branca.element.IFrame(html=html, width=400, height=300)
    popup=fo.Popup(iframe, parse_html=True)
    fo.Marker(location=[volcano['Latitude'].iloc[i], volcano['Longitude'].iloc[i]],popup=popup, tooltip='click me!', icon=fo.Icon(color=death(i), icon='volcano')).add_to(map)


# In[17]:


def death(number):
    if (number<5):
        return 'blue'
    elif(number>5 and number<30):
        return 'green'
    else:
        return 'red'
    
    


# In[18]:


x.add_child(fo.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))


# In[26]:


map.add_child(x)


# In[7]:





# In[ ]:





# In[5]:


cd desktop


# In[ ]:





# In[14]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




