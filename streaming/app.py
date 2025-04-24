import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import singlestoredb as s2
import os
from dotenv import load_dotenv

load_dotenv(override=True)

config = {
    "host": os.getenv('host'),
    "port": os.getenv('port'),
    "user": os.getenv('user'),
    "password": os.getenv('password'),
    "database": os.getenv('database')
}

def fetch_data():
    query = """
    SELECT localTS, ticker, price, size
      FROM live_trades
     WHERE localTS >= CONVERT_TZ(NOW(), @@session.time_zone, 'America/New_York')
                       - INTERVAL 10 MINUTE
     ORDER BY localTS
    """
    conn = s2.connect(**config)
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()
    if not df.empty:
        df['localTS'] = pd.to_datetime(df['localTS'])
        df.sort_values('localTS', inplace=True)
    return df

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='ticker-dropdown',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'AAPL', 'value': 'AAPL'},
            {'label': 'MSFT', 'value': 'MSFT'},
            {'label': 'NVDA', 'value': 'NVDA'},
            {'label': 'TSLA', 'value': 'TSLA'},
            {'label': 'AMZN', 'value': 'AMZN'}
        ],
        value='ALL',
        clearable=False
    ),
    dcc.Graph(id='live-trades-graph'),
    dcc.Interval(id='interval-component', interval=1_000, n_intervals=0)
])

@app.callback(
    Output('live-trades-graph', 'figure'),
    Input('interval-component', 'n_intervals'),
    Input('ticker-dropdown', 'value')
)
def update_graph_live(n, selected_ticker):
    df = fetch_data()
    if selected_ticker != 'ALL':
        df = df[df['ticker'] == selected_ticker]
    if df.empty:
        fig = px.line(title="No Data Available")
        fig.update_layout(xaxis_title="Timestamp", yaxis_title="Price")
        return fig

    fig = px.line(df, x='localTS', y='price', color='ticker',
                  title=f"Live Trades ({selected_ticker if selected_ticker!='ALL' else 'All'})")
    fig.update_traces(connectgaps=True)
    fig.update_xaxes(
        range=[df['localTS'].min(), df['localTS'].max()],
        tickformat='%H:%M:%S',
        nticks=6,
        tickangle=45,
        rangeslider_visible=False
    )
    fig.update_layout(xaxis_title="Timestamp", yaxis_title="Price")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)