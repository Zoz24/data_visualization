from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result', 'dtick': 1}
y_axis_config = {'title': 'frequency of result'}
my_layout = Layout(title='results of rolling d6 and d10 50000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6_d10.html')