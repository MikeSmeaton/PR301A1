from ChartOutputController import ChartController

createChart = ChartController(['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
createChart.get_pie_chart()
createChart.get_bar_graph()

createChart2 = ChartController(['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
createChart2.get_scatter_graph()