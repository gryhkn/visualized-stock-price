# Visualized Simple Stock Price Web App

This is a simple Streamlit web app where you can see and compare the closing prices and volumes of different companies' stocks. The data for this project is fetched from Yahoo Finance using the yfinance library.

![](https://github.com/gryhkn/VisualizedStockPrice/blob/master/ss/stock%20data.png?raw=true)

## Features
- Choose a company and view its closing price, volume, candlestick chart, and moving average.
- Compare the closing prices of multiple companies.
- Choose the period you want to view data from with a slider.

![](https://github.com/gryhkn/VisualizedStockPrice/blob/master/ss/compare.png?raw=true)

## Installation

Before running this project, you need to have Python and pip (Python's package installer) installed on your computer. If you don't have them installed, you can download Python [here](https://www.python.org/downloads/) and pip will be installed along with it.

You will also need to install the following Python libraries:

- yfinance
- streamlit
- plotly

You can install these libraries by running the following command in your terminal:

```sh
pip install yfinance pandas streamlit plotly
```

## Running the App

After you've installed the required libraries, you can run this app. To do this, you need to:

1) Download this project and open a terminal in the project's folder.
2) Run the following command:

```
streamlit run app.py
```

After a moment, the app will open in your default web browser.

## License
This project is licensed under the terms of the MIT license.