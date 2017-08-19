import plotly
import plotly.graph_objs as go


class BarGraph(object):

    def __init__(self, title,  labels, values, chart_names):
        self.title = title
        self.labels = labels
        self.values = values
        self.chart_names = chart_names

    def give_graph(self):

        trace = go.Bar(
            x=self.labels,
            y=self.values
        )

        data = [trace]
        layout = go.Layout(
            title=self.title,
            xaxis=dict(
                title=self.chart_names[0],
                titlefont=dict(
                    size=30
                )
            ),
            yaxis=dict(
                title=self.chart_names[1],
                titlefont=dict(
                    size=30
                )
            )
        )

        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='bar-graph.html')

    def test_title(self):
        return self.title


