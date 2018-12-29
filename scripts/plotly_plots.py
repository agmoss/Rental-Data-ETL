import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

def bar_community(df):

    data = df['community'].value_counts()[:20]

    plotly.offline.plot({
        "data" : [
        go.Bar(
            x=data.index,
            y=data.values
        )
        ],

        "layout" : go.Layout(title = "Communities with the Most Rental Listings",xaxis= dict(title= 'Community',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Number of Open Listings',ticklen= 5,zeroline= False))
                
    },filename='plotly_bar_community.html',auto_open=False)



def box_price_quadrant(df):

    plotly.offline.plot({
        "data" : [
        go.Box(
            x=df["quadrant"], 
            y=df["price"]
        )
        ],

        "layout" : go.Layout(title = "Price Distribution Per Quadrant",xaxis= dict(title= 'City Quadrant',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Price',ticklen= 5,zeroline= False))
                
    },filename='plotly_box_price_quadrant_.html',auto_open=False)


def distplot(df):

    # In the works

    data = df['price']

    data = [data]
    group_labels = ['Price']

    fig = ff.create_distplot(data,group_labels)

    plotly.offline.plot(fig, filename='test2',auto_open=False)


if __name__ == "__main__":

    print(__name__)