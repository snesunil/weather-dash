import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the weather dataset
temp_df = pd.read_csv("../data/weather_pro.csv", parse_dates=True)

# Define the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

server = app.server

# Title
app.title = "US Weather Dashboard"

# Define the layout
app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "US Weather Dashboard",
                            style={"font-weight": "bold",
                                "padding": 20,
                                "color": "black",
                                "margin-left": 15,
                                "text-align": "center",
                                "font-size": "36px",
                                "border-radius": 1,
                            },
                        )
                    ],
                    width=12,
                )
            ]
        ),
        dbc.Container(
            [
                    dbc.Row(
                        [
                            dbc.Col(html.H5("Select a State", style={"font-weight": "bold"}), width=2),
                            dbc.Col(
                                dcc.Dropdown(
                                    id="state-dropdown",
                                    options=[
                                        {"label": state, "value": state}
                                        for state in temp_df["state"].unique()
                                    ],
                                    value="NJ",
                                ),
                                width=2,
                            ),
                        ]
                    )
                ,
        html.Br()
            ]
        ),
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H4(
                                            "Avg Temperature in the state by month",
                                            className="card-title",
                                            style={"color": "black"},
                                        ),
                                        style={"background-color": "#FF7D33"},
                                    ),
                                    dcc.Graph(id="bar-plot", style={"height": "600px"}),
                                ]
                            )
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H4(
                                            "Distribution of temperature in Cities",
                                            className="card-title",
                                            style={"color": "black"},
                                        ),
                                        style={"background-color": "#FF7D33"},
                                    ),
                                    dcc.Graph(id="new-plot", style={"height": "600px"}),
                                ]
                            )
                        ],
                        width=6,
                    ),
                ]
            )
        ),
        html.Br(),
        dbc.Container([
            dbc.Row(
                [
                    dbc.Col(dbc.Row([ html.H5("Select City 1", style={"font-weight": "bold"}),dcc.Dropdown(id="city1-dropdown")])),
                    dbc.Col(dbc.Row([ html.H5("Select City 2", style={"font-weight": "bold"}),dcc.Dropdown(id="city2-dropdown")])),
                ]
            ),
    ]),
        html.Br(),
        dbc.Container( dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H4(
                                            "Comparison of Temperature Trends for Selected Cities",
                                            className="card-title",
                                            style={"color": "black"},
                                        ),
                                        style={"background-color": "#FF7D33"},
                                    ),
                                    dcc.Graph(id="line-plot", style={"height": "600px"}),
                                ]
                            )),
    ]
)

# Define the callback to update the new plot
@app.callback(
    dash.dependencies.Output("bar-plot", "figure"),
    [dash.dependencies.Input("state-dropdown", "value")],
)
def update_bar_plot(state):
    grp_df = temp_df[temp_df["state"] == state]
    temp_grouped = grp_df.groupby("month")["temp_c"].mean().reset_index()

    fig = px.bar(
        temp_grouped,
        x="temp_c",
        y="month",
        orientation="h",
        title=f"",
        text=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        color="month",
    )

    fig.update_yaxes(showticklabels=False)
    fig.update_traces(showlegend=False)

    # Update the layout
    fig.update_layout(
        xaxis_title="Temperature(°C)", yaxis_title="Months",
          showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False),
        xaxis=dict(showgrid=True,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        tickwidth=1,
        ticklen=5)
    )

    return fig


@app.callback(
    [
        dash.dependencies.Output("city1-dropdown", "options"),
        dash.dependencies.Output("city1-dropdown", "value"),
    ],
    [dash.dependencies.Input("state-dropdown", "value")],
)
def update_city_options(selected_state):
    cities = temp_df[temp_df["state"] == selected_state]["city"].unique()
    return ([{"label": city, "value": city} for city in cities], cities[0])


@app.callback(
    [
        dash.dependencies.Output("city2-dropdown", "options"),
        dash.dependencies.Output("city2-dropdown", "value"),
    ],
    [dash.dependencies.Input("state-dropdown", "value")],
)
def update_city_options(selected_state):
    cities = temp_df[temp_df["state"] == selected_state]["city"].unique()
    return ([{"label": city, "value": city} for city in cities], cities[0])


# Create callback to update line plot based on selected cities
@app.callback(
    dash.dependencies.Output("line-plot", "figure"),
    [
        dash.dependencies.Input("city1-dropdown", "value"),
        dash.dependencies.Input("city2-dropdown", "value"),
    ],
)
def update_line_plot(city_1, city_2):
    city_df = temp_df[~temp_df["date"].str.contains("2022")]
    city_df = city_df.query(
        "city == @city_1 or city == @city_2 and high_or_low == 'high'"
    )
    city_df = city_df.groupby(["month", "city"])["temp_c"].mean().reset_index()

    fig = px.line(
        city_df,
        x="month",
        y="temp_c",
        color="city"
    )

    
    fig.update_traces(line=dict(width=7))

    fig.update_layout(showlegend=True,
        yaxis_title="Temperature(°C)", xaxis_title="Months",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=True,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        tickwidth=1,
        ticklen=5),
        xaxis=dict(showgrid=True,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        tickwidth=1,
        ticklen=5)
        )
    return fig


# Define the callback to update the new plot
@app.callback(Output("new-plot", "figure"), Input("state-dropdown", "value"))
def update_new_plot(state):
    state_df = temp_df[(temp_df["state"] == state)]

    df = state_df
    fig = px.violin(df, y="city", x="temp_c", box=True, color="city")

    # Update the layout
    fig.update_layout(
        xaxis_title="Temperature(°C)", yaxis_title="Cities", showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False),
        xaxis=dict(showgrid=True,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        tickwidth=1,
        ticklen=5)
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
