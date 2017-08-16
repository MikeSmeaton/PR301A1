import plotly.graph_objs as go
import plotly


class BoxPlot(object):

    def __init__(self, title, values, values_two, chart_names):
        self.values_two = values_two
        self.title = title
        self.values = values
        self.chart_names = chart_names

    def give_graph(self):

        trace0 = go.Box(
            y=self.values,
            name = self.chart_names[0]
        )
        trace1 = go.Box(
            y=self.values_two,
            name=self.chart_names[1]
        )
        data = [trace0, trace1]

        layout = go.Layout(
            title=self.title,
        )

        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='box-plot.html')