from ChartOutputController import ChartController
from FileHandler import FileHandler

file = FileHandler('written_file.csv')
file_array = file.get_file()
print(file_array)

bar = ChartController('This is a bar graph')
bar.get_bar_graph(file_array[0], file_array[1], file_array[2])

pie = ChartController('This is a pie chart')
pie.get_pie_chart(['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500])

scatter = ChartController('This is a scatter graph')
scatter.get_scatter_graph(['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])

box = ChartController('This is a box plot')
box.get_box_plot([4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
