import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pd.read_csv("reviews.csv",parse_dates=['Timestamp'])

#Grouping based on month
data['Month'] = data["Timestamp"].dt.strftime("%Y-%m")

ratings = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()
print(ratings)

chartDef = """{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating For The Courses'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
           '#FFFFFF'
    },
    xAxis: {
        categories: []
        ,
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: []
}"""


def app():
    webPage = jp.QuasarPage()
    h1 = jp.QDiv(a=webPage,text="Data Analysis",classes="text-h4 text-center q-pa-md")
    hightChart = jp.HighCharts(a=webPage,options=chartDef)
    hightChart.options.title.text = "Reviews Data-Analysis"
    
    chartData = [{"name":val,"data":[rating for rating in ratings[val] ]} for val in ratings.columns]
    
    hightChart.options.xAxis.categories= list(ratings.index)
    hightChart.options.series = chartData

    
    return webPage

jp.justpy(app)
    