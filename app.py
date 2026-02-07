from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df=pd.read_csv("filtered_file.csv")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")
df = df.groupby("Date", as_index=False)["Sales"].sum()
df = df.resample("ME", on="Date")["Sales"].sum().reset_index()




cutoff_date = pd.to_datetime("2021-01-15")

df["Period"] = np.where(df["Date"] < cutoff_date, "Before", "After")

fig=px.line(df,x='Date',y='Sales',color='Period',color_discrete_map={
        "Before": "yellow",
        "After": "aqua"
    },markers=True)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales Before And After 15th Jan 2021',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

