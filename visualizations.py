import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def process_data():
    """ extract data from csv file, and process data into workable & graph-able data """

    # Extract data from CSV with semicolon separator
    monthly_data = pd.read_csv("SN_m_tot_V2.0.csv", sep=';')
    # Assign column names
    monthly_data.columns = ['Year', 'Month', 'Frac_Date', 'Monthly_Total_Sunspot', 'Standard_Dev',
                            'Num_Observations', 'Provisional_Indicator']
    # Return the processed data frame
    return monthly_data


def plot_data(begin_date, end_date, window):
    """
    plot both the total sunspot activity and the smoothed sunspot activity
    based on the interval given.

    Arguments:
    begin_date (int): begin year for data interval
    end_date (int): end year for data interval
    window (int): how many months to smooth

    Return:
    graph figure
    """
    # Get data from process_data()
    df_data = process_data()

    # Cut the df into specific interval
    interval_data = df_data[(df_data['Year'] >= begin_date) & (df_data['Year'] < end_date)]

    # From the sliced interval, calculate the running average
    interval_data['Smoothed'] = interval_data['Monthly_Total_Sunspot'].rolling(window=window).mean()

    # Create two figures in one graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=interval_data['Frac_Date'], y=interval_data['Monthly_Total_Sunspot'], mode='lines', name='Total Sunspot'))
    fig.add_trace(go.Scatter(x=interval_data['Frac_Date'], y=interval_data['Smoothed'], mode='lines', name='Smoothed Curve'))

    # Return figure
    return fig


def plot_cycle(cycle):
    """
    Plots the sunspot activity with given amount of cycle years

    Argument:
    cycle (int): years for one cycle

    Return:
    graph figure
    """
    # Get data from process_data()
    df_data = process_data()

    # Calculate cycle years
    df_data['Cycle_Years'] = df_data['Frac_Date'] % cycle

    # Create scatter plot
    fig = px.scatter(df_data, x='Cycle_Years', y='Monthly_Total_Sunspot')

    # Return figure
    return fig
