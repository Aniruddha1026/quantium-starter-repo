from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#header", timeout=10)


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#sales-graph", timeout=10)


def test_radio_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#region-radio", timeout=10)

