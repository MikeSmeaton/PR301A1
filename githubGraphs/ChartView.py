from ChartOutputController import ChartController
from FileHandler import FileHandler
"""
file = FileHandler('written_file.txt')
file.write_file()"""

bar = ChartController('This is a bar graph')
bar.get_bar_graph(['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], ['words name', 'Numbers Names'])

pie = ChartController('This is a pie chart')
pie.get_pie_chart(['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500])

scatter = ChartController('This is a scatter graph')
scatter.get_scatter_graph(['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])

box = ChartController('This is a box plot')
box.get_box_plot([4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])