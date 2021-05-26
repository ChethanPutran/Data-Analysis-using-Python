import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pd.read_csv("reviews.csv",parse_dates=['Timestamp'])

#Grouping based on month
data['Month'] = data["Timestamp"].dt.strftime("%Y-%m")

ratings = data.groupby(['Month','Course Name'])['Rating'].count().unstack()
# print(ratings)

chartDef = """{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },
    title: {
        floating: true,
        align: 'left',
        text: ''
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: ''
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },


    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}"""


def app():
    webPage = jp.QuasarPage()
    h1 = jp.QDiv(a=webPage,text="Data Analysis",classes="text-h4 text-center q-pa-md")
    h1 = jp.QDiv(a=webPage,text="Reviews Data-Analysis",classes="text-h5 text-center q-pa-md")
    hightChart = jp.HighCharts(a=webPage,options=chartDef)
    
    
    chartData = [{"name":val,"data":[rating for rating in ratings[val] ]} for val in ratings.columns]
    
    hightChart.options.xAxis.categories= list(ratings.index)
    hightChart.options.series = chartData

    
    return webPage

jp.justpy(app)
    