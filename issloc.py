import plotly.express as px
import pandas as pd
url = 'http://open-notify.org/Open-Notify-API/ISS-Location-Now/'
df = pd.read_json(url)
print(df)