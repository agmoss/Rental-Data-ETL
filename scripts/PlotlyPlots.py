import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

class PlotlyPlots:

    def __init__(self,df,write_path):
        self.df = df
        self.write_path = write_path


    def bar_community(self):
        
        data = self.df['community'].value_counts()[:20]

        a = plotly.offline.plot({
            "data" : [
            go.Bar(
                x=data.index,
                y=data.values
            )
            ],

            "layout" : go.Layout(title = "Communities with the Most Rental Listings",xaxis= dict(title= 'Community',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Number of Open Listings',ticklen= 5,zeroline= False))
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a

    def box_price_quadrant(self):

        a = plotly.offline.plot({
            "data" : [
            go.Box(
                x=self.df["quadrant"], 
                y=self.df["price"]
            )
            ],

            "layout" : go.Layout(title = "Price Distribution Per Quadrant",xaxis= dict(title= 'City Quadrant',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Price',ticklen= 5,zeroline= False))
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a

    def distplot(self):

        # In the works

        a = data = self.df['price']

        data = [data]
        group_labels = ['Price']

        fig = ff.create_distplot(data,group_labels)

        plotly.offline.plot(fig,include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a 