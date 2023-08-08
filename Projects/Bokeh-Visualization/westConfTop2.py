# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Import the data
from readNbaData import west_top_2

# Output to static HTML file
output_file('west_top_2_standings_race.html',
            title='Western Conference Top 2 Teams Wins Race')

# Isolate the data for the Rockets and Warriors
rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

# Create a ColumnDataSource object for each team
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

# Create and configure the figure
fig = figure(x_axis_type='datetime',
             height=300,
             width=600,
             title='Western Conference Top 2 Teams Wins Race, 2017-18',
             x_axis_label='Date',
             y_axis_label='Wins',
             toolbar_location=None)

# Render the race as step lines
fig.step('stDate', 'gameWon',
         color='#CE1141',
         legend_label='Rockets',
         source=rockets_cds)

fig.step('stDate', 'gameWon',
         color='#006BB6',
         legend_label='Warriors',
         source=warriors_cds)

# Move the legend to the upper left corner
fig.legend.location = 'top_left'

# Show the plot
show(fig)
