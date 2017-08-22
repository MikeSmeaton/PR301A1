import plotly.graph_objs as go
import plotly
import os.path


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
        plotly.offline.plot(fig, filename=self.title + '.html')

        if (os.path.exists(self.title + '.html')):
            return True

    def test_title(self):
        return self.title

    def test_labels(self):
        return self.labels

    def test_values(self):
        return self.values
