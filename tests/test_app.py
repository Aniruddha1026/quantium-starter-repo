from app import update_graph
import plotly.graph_objects as go

def test_update_graph_returns_figure():
    fig = update_graph("South")

    assert isinstance(fig, go.Figure)
