# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Import the data
from read_nba_data import standings

# Output to static HTML file
output_file('east_top_2_standings_race.html',
            title='Eastern Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create view for each team
celtics_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='TOR')])

# Create and configure the figure
east_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Eastern Conference Top 2 Teams Wins Race, 2017-18',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)

# Render the race as step lines
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=celtics_view,
              color='#007A33', legend_label='Celtics')
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=raptors_view,
              color='#CE1141', legend_label='Raptors')

# Move the legend to the upper left corner
east_fig.legend.location = 'top_left'

# Show the plot
show(east_fig)
