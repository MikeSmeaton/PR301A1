import unittest
from ChartOutputController import ChartController
from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot
from FileHandler import FileHandler


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_pie_title(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_title(),'pie title')

    def test_pie_labels(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_labels(), ['one', 'two'])

    def test_pie_values(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_values(), [1, 2])

    def test_bar_title(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_title(),'bar title')

    def test_bar_labels(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_labels(), ['one', 'two'])

    def test_bar_values(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_values(), [1, 2])

    def test_bar_names(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_names(), ['chart name 1', 'chart name 2'])

    def test_box_title(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        self.assertEqual(box_plot.test_title(), 'box title')

    def test_box_values(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        self.assertEqual(box_plot.test_values(), [4500, 2500, 1200])

    def test_box_values_two(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        self.assertEqual(box_plot.test_values_two(), [500, 6000, 2400])

    def test_box_names(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        self.assertEqual(box_plot.test_names(), ['chart one', 'chart 2'])

    def test_scatter_title(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_title(), 'scatter title')

    def test_scatter_labels(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_labels(), ['Oxygen', 'Hydrogen'])

    def test_scatter_values(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_values(), [4500, 2500, 1053, 500])

    def test_scatter_values_two(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_values_two(), [500, 2400, 1453, 5700])

    def test_pie_build(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertTrue(pie_chart.give_graph())

    def test_bar_build(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertTrue(bar_graph.give_graph())

    def test_box_build(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        self.assertTrue(box_plot.give_graph())

    def test_scatter_build(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertTrue(scatter_graph.give_graph())

    def test_pie(self):
        pie = ChartController('This is a pie chart')
        self.assertTrue(pie.get_pie_chart(['one', 'two'], [1, 2]))

    def test_bar(self):
        bar = ChartController('This is a bar graph')
        self.assertTrue(bar.get_bar_graph(['one', 'two'], [1, 2], ['chart name 1', 'chart name 2']))

    def test_box(self):
        box = ChartController('This is a box chart')
        self.assertTrue(box.get_box_plot([4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2']))

    def test_scatter(self):
        scatter = ChartController('This is a scatter graph')
        self.assertTrue(scatter.get_scatter_graph(['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                                  [500, 2400, 1453, 5700]))

    def test_write_file(self):
        file = FileHandler('written_file1.csv')
        self.assertEqual(file.write_file('file content'), 'file content')

    def test_load_file(self):
        file = FileHandler('written_file.csv')
        self.assertEqual(file.get_file(), [['Oxygen', 'Hydrogen', 'Carbon_Dioxide'], ['4500', '2500', '1053'],
                                           ['words name', 'Number Names', 'None']])


if __name__ == '__main__':
    unittest.main()