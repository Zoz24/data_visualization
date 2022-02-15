from matplotlib.axis import YAxis
from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result'}
y_axis_config = {'title': 'frequency of result'}
my_layout = Layout(title='results of rolling a dice 1000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6.html')