import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt



data = pd.read_csv("reviews.csv",parse_dates=['Timestamp'])

#Grouping based on month
data['Month'] = data["Timestamp"].dt.strftime("%Y-%m")
data_mon = data.groupby(['Month']).mean()
# data.head()

chartDef = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Reviews Status'
    },
    subtitle: {
        text: 'Data-Analysis for reviews'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Ratings',
        data:[]
    }]
}
"""

def app():
    webPage = jp.QuasarPage()
    h1 = jp.QDiv(a=webPage,text="Data Analysis",classes="text-h4 text-center q-pa-md")
    hightChart = jp.HighCharts(a=webPage,options=chartDef)
    hightChart.options.title.text = "Reviews Data-Analysis"
    
    hightChart.options.xAxis.categories= list(data_mon.index)
    hightChart.options.series[0].data = list(data_mon["Rating"])
    
    return webPage

jp.justpy(app)
