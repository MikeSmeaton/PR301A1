"""
>>> from ChartOutputController import ChartController
>>> from PieChart import PieChart
>>> from BarGraph import BarGraph
>>> from ScatterGraph import ScatterGraph
>>> from BoxPlot import BoxPlot
>>> from FileHandler import FileHandler

>>> pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
>>> pie_chart.test_title()
'pie title'
>>> pie_chart.test_labels()
['one', 'two']
>>> pie_chart.test_values()
[1, 2]

>>> bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
>>> bar_graph.test_title()
'bar title'
>>> bar_graph.test_labels()
['one', 'two']
>>> bar_graph.test_values()
[1, 2]
>>> bar_graph.test_names()
['chart name 1', 'chart name 2']

>>> box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
>>> box_plot.test_title()
'box title'
>>> box_plot.test_values()
[4500, 2500, 1200]
>>> box_plot.test_values_two()
[500, 6000, 2400]
>>> box_plot.test_names()
['chart one', 'chart 2']

>>> scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
>>> scatter_graph.test_title()
'scatter title'
>>> scatter_graph.test_labels()
['Oxygen', 'Hydrogen']
>>> scatter_graph.test_values()
[4500, 2500, 1053, 500]
>>> scatter_graph.test_values_two()
[500, 2400, 1453, 5700]

>>> pie_chart.give_graph()
True

>>> bar_graph.give_graph()
True

>>> box_plot.give_graph()
True

>>> scatter_graph.give_graph()
True

>>> pie = ChartController('This is a pie chart')
>>> pie.get_pie_chart(['one', 'two'], [1, 2])
Pie Chart Made!
True

>>> bar = ChartController('This is a bar graph')
>>> bar.get_bar_graph(['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
Bar Graph Made!
True

>>> box = ChartController('This is a box chart')
>>> box.get_box_plot([4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
Box Plot Made!
True

>>> scatter = ChartController('This is a scatter graph')
>>> scatter.get_scatter_graph(['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
Scatter Graph Made!
True

>>> file = FileHandler('written_file1.csv')
>>> file.write_file('file content')
'file content'

>>> file = FileHandler('written_file.csv')
>>> file.get_file()
[['Oxygen', 'Hydrogen', 'Carbon_Dioxide'], ['4500', '2500', '1053'], ['words name', 'Number Names', 'None']]
"""