from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot


class ChartController(object):

    def __init__(self, title, labels, values, values_two, chart_names):
        self.title = title
        self.labels = labels
        self.values = values
        self.values_two = values_two
        self.chart_names = chart_names

    def get_pie_chart(self):
        pie_chart = PieChart(self.title, self.labels, self.values)
        pie_chart.give_graph()

    def get_bar_graph(self):
        bar_graph = BarGraph(self.title, self.labels, self.values, self.chart_names)
        bar_graph.give_graph()

    def get_scatter_graph(self):
        scatter_graph = ScatterGraph(self.title, self.labels, self.values, self.values_two)
        scatter_graph.give_graph()

    def get_box_plot(self):
        box_plot = BoxPlot(self.title, self.values, self.values_two, self.chart_names)
        box_plot.give_graph()

