# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import column, row

# Import the data
from readNbaData import standings

# Output to static HTML file
output_file('east__west_top_2_standings_race.html',
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
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

west_fig = figure(x_axis_type='datetime',
                  height=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

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

# Show the plot
show(column(west_fig, east_fig))
