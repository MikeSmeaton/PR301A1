import plotly
import plotly.graph_objs as go
import os.path


class ScatterGraph(object):

    def __init__(self, title, labels, values, values_two):
        self.title = title
        self.labels = labels
        self.values = values
        self.values_two = values_two

    def give_graph(self):
        trace = go.Scatter(
            x=self.values,
            y=self.values_two,
            mode='markers'
        )

        data = [trace]

        layout = go.Layout(
            title=self.title,
            xaxis=dict(
                title=self.labels[0],
                titlefont=dict(
                    size=30
                )
            ),
            yaxis=dict(
                title=self.labels[1],
                titlefont=dict(
                    size=30
                )
            )
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

    def test_values_two(self):
        return self.values_two
