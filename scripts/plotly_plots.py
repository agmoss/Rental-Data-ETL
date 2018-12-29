import plotly
import plotly.graph_objs as go

def bar_community(df):

    # The axes of this plot are incorrect...

    data = [
        go.Bar(
            x=df['community'],
            y=df['community'].value_counts()
        )
    ]

    plotly.offline.plot(data, filename='test',auto_open=False)


def box_price_quadrant_interactive(df):

    # This one works...

    data = [
        go.Box(
        x=df["quadrant"], 
        y=df["price"]
        )
    ]

    plotly.offline.plot(data, filename='test1',auto_open=False)

if __name__ == "__main__":

    print(__name__)