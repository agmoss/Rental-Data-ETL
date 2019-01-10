import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np

class PlotlyPlots:

    def __init__(self,df,write_path):
        self.df = df
        self.write_path = write_path
        # keep rows that are within +3 to -3 standard deviations in the column 'Price'
        self.df1 =  df[np.abs(df.price-df.price.mean()) <= (3 * df.price.std())]


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
                x=self.df1["quadrant"], 
                y=self.df1["price"]
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

    def bar_price_community(self):

        df2 = self.df1.groupby('community', as_index=False)['price'].mean()

        df2 = df2.sort_values('price')

        a = plotly.offline.plot({
            "data" : [
            go.Bar(
                y=df2["community"], 
                x=df2["price"],
                orientation='h'
            )
            ],

            "layout" : go.Layout(title = "Average Price Per Community",xaxis= dict(title= 'Price',ticklen= 5,zeroline= False),
                yaxis= dict(title= 'Community',ticklen= 5,zeroline= False))
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a

    def pie_community(self):

        data = self.df['community'].value_counts()[:10]

        a = plotly.offline.plot({
            "data" : [
            go.Pie(
                labels=data.index,
                values=data.values
            )
            ],

            "layout" : go.Layout(title = "Communities with the Most Rental Listings")
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a