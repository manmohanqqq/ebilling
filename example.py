import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import time

# Generate random electricity consumption data
def generate_electricity_data():
    today = datetime.date.today()
    np.random.seed(today.toordinal())  # Ensure different data each day
    data = {
        "Date": pd.date_range(start=today - datetime.timedelta(days=29), periods=30, freq='D'),
        "Consumption (kWh)": np.random.randint(100, 500, 30),
        "Cost (₹)": np.random.randint(500, 2000, 30)
    }
    return pd.DataFrame(data)

# Generate random appliance-wise consumption data
def generate_appliance_data():
    appliances = ['AC', 'Refrigerator', 'Washing Machine', 'Heater', 'TV', 'Fan', 'Lights',
                  'Microwave', 'Laptop', 'Iron', 'Geyser', 'Vacuum Cleaner', 'Toaster']
    today = datetime.date.today()
    np.random.seed(today.toordinal())
    data = {
        "Date": [today - datetime.timedelta(days=i) for i in range(30)],
        "Appliance": np.random.choice(appliances, 30),
        "Consumption (kWh)": np.random.randint(5, 100, 30)
    }
    return pd.DataFrame(data)

df_electricity = generate_electricity_data()
df_appliance = generate_appliance_data()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Electricity Consumption Analysis"),
    
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # Refresh every 10 seconds
        n_intervals=0
    ),
    
    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': 'Consumption (kWh)', 'value': 'Consumption (kWh)'},
            {'label': 'Cost (₹)', 'value': 'Cost (₹)'}
        ],
        value='Consumption (kWh)',
        clearable=False
    ),
    dcc.Graph(id='power-chart'),
    
    html.H3("Appliance-wise Consumption"),
    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=df_appliance['Date'].min(),
        max_date_allowed=df_appliance['Date'].max(),
        start_date=df_appliance['Date'].min(),
        end_date=df_appliance['Date'].max()
    ),
    dcc.Graph(id='appliance-chart')
])

@app.callback(
    Output('power-chart', 'figure'),
    Input('chart-type', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_power_chart(selected_value, n):
    global df_electricity
    df_electricity = generate_electricity_data()
    fig = px.line(df_electricity, x='Date', y=selected_value, title=f'{selected_value} Over Time')
    return fig

@app.callback(
    Output('appliance-chart', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('interval-component', 'n_intervals')]
)
def update_appliance_chart(start_date, end_date, n):
    global df_appliance
    df_appliance = generate_appliance_data()
    filtered_df = df_appliance[(df_appliance['Date'] >= start_date) & (df_appliance['Date'] <= end_date)]
    fig = px.bar(filtered_df, x='Appliance', y='Consumption (kWh)', title='Appliance-wise Consumption')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)