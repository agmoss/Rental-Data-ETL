import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np


class PlotlyPlots:

    def __init__(self,df):
        self.df = df
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

            "layout" : go.Layout(xaxis= dict(title= 'Community',ticklen= 5,zeroline= False),
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

            "layout" : go.Layout(
                xaxis= dict(title= 'City Quadrant',ticklen= 5,zeroline= False,automargin = True),
                yaxis= dict(title= 'Price',ticklen= 5,zeroline= False,automargin = True),
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=25,
                    t=25,
                    pad=4
                        )
                )
                    
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

    def scatter_price_community(self):

        df2 = self.df1.groupby('community', as_index=False)['price'].mean()

        df2 = df2.sort_values('price')

        a = plotly.offline.plot({
            "data" : [
            go.Scatter(
                y=df2["community"], 
                x=df2["price"],
                marker =  {"color": "red", "size": 12},
                mode = "markers"
                
            )
            ],

            "layout" : go.Layout(
                xaxis= dict(title= 'Price',ticklen= 5,zeroline= False,automargin = True),
                yaxis= dict(title= 'Community',ticklen= 5,zeroline= False,automargin = True),
                autosize=False,
                width=1100,
                height=500,
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=25,
                    t=25,
                    pad=4
                        )
                )
                    
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

            "layout" : go.Layout(
                autosize=False,
                width=400,
                height=400,
                legend=dict(orientation="h"),
                margin=go.layout.Margin(
                    l=5,
                    r=5,
                    b=5,
                    t=5,
                    pad=1
                        )
                )
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a

    def corr_heatmap(self):


        corr = self.df.corr()


        colorscale = [[0, '#edf8fb'], [.3, '#b3cde3'],  [.6, '#8856a7'],  [1, '#810f7c']]

        a = plotly.offline.plot({
            "data" : [
            go.Heatmap(
                z = corr.values,
                x = corr.columns, 
                y = corr.index, 
                colorscale=colorscale

            )
            ],

            "layout" : go.Layout(
                autosize=False,
                width=500,
                height=500,
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=50,
                    t=50,
                    pad=10
                        )
                )
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a


    def hist(self):

        data = self.df['price']

        a = plotly.offline.plot({
            "data" : [
            go.Histogram(
                x=self.df1["price"]
            )
            ],

            "layout" : go.Layout(
                xaxis= dict(title= 'Price',ticklen= 5,zeroline= False,automargin = True),
                yaxis= dict(title= 'Frequency',ticklen= 5,zeroline= False,automargin = True),
                margin=go.layout.Margin(
                    l=50,
                    r=50,
                    b=25,
                    t=25,
                    pad=4
                        )
                )
                    
        },include_plotlyjs=False, output_type='div',auto_open=False, config={"displayModeBar": False},show_link=False)

        return a
