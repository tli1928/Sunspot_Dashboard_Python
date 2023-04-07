from dash import Dash, dcc, html, Input, Output
import visualizations

# create app
app = Dash(__name__)

# Create a mark dictionary for customizing dashboard slider
mark = {1800: '1800',
        1825: '1825',
        1850: '1850',
        1875: '1875',
        1900: '1900',
        1925: '1925',
        1950: '1950',
        1975: '1975',
        2000: '2000',
        2020: '2020'}

# define app layout
app.layout = html.Div([
    # first visual: sunspot activity
    html.H1('Sundash: Monitoring and Analyzing Solar Activity'),
    dcc.Graph(id='sunspot'),
    dcc.Interval(id='interval', interval=100, n_intervals=0),
    html.P('Which year to begin?'),
    dcc.RangeSlider(id='year_range', min=1800, max=2020, step=20, value=[1850, 2000], marks=mark),
    html.P('How smooth?'),
    dcc.Slider(id='smooth_idx', min=1, max=30, step=1, value=12),

    # second visual: year cycles
    dcc.Graph(id='cycles'),
    dcc.Interval(id='interval', interval=100, n_intervals=0),
    html.P('How many years for one cycle?'),
    dcc.Slider(id='cycle_year', min=1, max=15, step=1, value=11),

    # insert picture into dashboard
    html.P('Current Real Image of the Sun'),
    html.Img(src="https://soho.nascom.nasa.gov/data/realtime/hmi_igr/1024/latest.jpg", style={'height': '20%',
                                                                                           'width': '20%'}),
    html.P('A 360 Degree View of the Sun'),
    html.Img(src='https://cdn.mos.cms.futurecdn.net/7nvSn2t3q7bjkZGMvRzh9M.gif')
])


# Establish connection between dashboard inputs and function inputs
@app.callback(
    Output('sunspot', 'figure'),
    Input('year_range', 'value'),
    Input('smooth_idx', 'value')
)
def update_sunspot(year_range, smooth_idx):
    """ Update sunspot figure on dashboard

    Arguments:
        year_range (list): a list of two int, begin year & end year interval
        smooth_idx (int): how smooth the data is

    Return:
        graph figure
    """
    # create figure via plot_data in visualizations.py
    fig = visualizations.plot_data(year_range[0], year_range[1], smooth_idx)

    return fig


# Establish connection between dashboard inputs and function inputs
@app.callback(
    Output('cycles', 'figure'),
    Input('cycle_year', 'value')
)
def update_cycle_year(cycle_year):
    """ Update sunspot figure on dashboard

    Arguments:
        cycle_year (list): number of years for one cycle

    Return:
        graph figure
    """
    # create figure via plot_cycle in visualizations.py
    fig = visualizations.plot_cycle(cycle_year)

    return fig


# run app server
app.run_server(debug=True)
