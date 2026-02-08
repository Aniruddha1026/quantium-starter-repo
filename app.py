from dash import Dash, html, dcc,Input,Output
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
df = df.groupby(["Date","Region"], as_index=False)["Sales"].sum()
df = (
    df.set_index("Date")
      .groupby("Region")
      .resample("ME")["Sales"]
      .sum()
      .reset_index()
)




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

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

        html.H1(
            id="header",
            children='Sales Before And After 15th Jan 2021',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div([

            html.H3(
                "Select Region",
                style={
                    'color': colors['text'],
                    'marginBottom': '10px'
                }
            ),

            dcc.RadioItems(
                id="region-radio",
                options=[
                    {"label": "North", "value": "North"},
                    {"label": "South", "value": "South"},
                    {"label": "East", "value": "East"},
                    {"label": "West", "value": "West"},
                    {"label": "All", "value": "All"},
                ],
                value="All",
                inline=True,
                labelStyle={
                    "marginRight": "20px",
                    "cursor": "pointer",
                    "color": colors['text']
                }
            )

        ], style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
        }),

        dcc.Graph(id="sales-graph")

    ]
)

@app.callback(
    Output("sales-graph","figure"),
    Input("region-radio","value"),
)
def update_graph(selected_region):
    if selected_region == "All":
        filtered_df = (
            df.groupby("Date", as_index=False)["Sales"]
            .sum()
            .copy()
        )
    else:
        filtered_df = df[df["Region"] == selected_region].copy()

    cutoff_date = pd.to_datetime("2021-01-15")

    filtered_df["Period"] = np.where(
        filtered_df["Date"] < cutoff_date,
        "Before",
        "After"
    )

    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        color='Period',
        color_discrete_map={
            "Before": "yellow",
            "After": "aqua"
        },
        markers=True
    )

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig    



if __name__ == '__main__':
    app.run(debug=True)

