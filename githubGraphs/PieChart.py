import plotly.graph_objs as go
import plotly


class PieChart(object):

    def __init__(self, title,  labels, values):
        self.title = title
        self.labels = labels
        self.values = values

    def give_graph(self):
        trace = go.Pie(labels=self.labels, values=self.values)

        data = [trace]

        layout = go.Layout(
            title=self.title,
        )

        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='pie-chart.html')



"""LAYOUT:
pie = PieChart(['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500])
pie.give_graph()"""
