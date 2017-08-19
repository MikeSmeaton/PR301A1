import plotly
import plotly.graph_objs as go


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
        plotly.offline.plot(fig, filename='scatter.html')