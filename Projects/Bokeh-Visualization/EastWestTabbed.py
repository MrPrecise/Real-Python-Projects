# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models.widgets import Panel, Tabs

# Import the data
from readNbaData import standings

# Output to static HTML file
output_file('east_west_top_2_tabbed_layout.html',
            title='Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create view for each team
celtics_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='TOR')])
rockets_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type='datetime',
                  heigh=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

west_fig = figure(x_axis_type='datetime',
                  heigh=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

# Increase the plot widths
east_fig.width = west_fig.width = 800

# Render the race as step lines
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=celtics_view,
              color='#007A33', legend_label='Celtics')
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=raptors_view,
              color='#CE1141', legend_label='Raptors')
west_fig.step('stDate', 'gameWon',
              source=standings_cds, view=rockets_view,
              color='#CE1141', legend_label='Rockets')
west_fig.step('stDate', 'gameWon',
              source=standings_cds, view=warriors_view,
              color='#006BB6', legend_label='Warriors')

# Move the legend to the upper left corner
east_fig.legend.location = 'top_left'
west_fig.legend.location = 'top_left'

# Create two panels, one for each conference
east_panel = Panel(child=east_fig, title='Eastern Conference')
west_panel = Panel(child=west_fig, title='Western Conference')

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)
