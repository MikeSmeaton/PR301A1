from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot


class ChartController(object):

    def __init__(self, title):
        self.title = title

    def get_pie_chart(self, labels, values):
        try:
            pie_chart = PieChart(self.title, labels, values)
            pie_chart.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in pie chart")
            return False
        else:
            print("Pie Chart Made!")
            return True

    def get_bar_graph(self, labels, values, chart_names):
        try:
            bar_graph = BarGraph(self.title, labels, values, chart_names)
            bar_graph.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in bar graph")
            return False
        else:
            print("Bar Graph Made!")
            return True

    def get_scatter_graph(self, labels, values, values_two):
        try:
            scatter_graph = ScatterGraph(self.title, labels, values, values_two)
            scatter_graph.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter graph")
            return False
        else:
            print("Scatter Graph Made!")
            return True

    def get_box_plot(self, values, values_two, chart_names):
        try:
            box_plot = BoxPlot(self.title, values, values_two, chart_names)
            box_plot.give_graph()
        except (ValueError, IndexError):
            print("Incorrect arguments in scatter plot")
            return False
        else:
            print("Box Plot Made!")
            return True
