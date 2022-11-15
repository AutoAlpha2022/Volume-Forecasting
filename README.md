# Time-Series-Forecasting
Trading Target(Volume/Volatility) Time Series Prediction in LOB


# Timeline:

## Week 2 Feature Engineering
* Indicators
  * aggressive buy, buy MO
  

## Week 1 Feature Engineering
* Simulator Improvement
  * Cross auction Implemention
  * Different type of clock in simulator
* [Time_Series_Transformer](https://huggingface.co/docs/transformers/model_doc/time_series_transformer)
* Clocks types
  * calender clock
  * volume clock
  * tick clock
* The timewindow size: 1m(default), 1s, 10s, 30s [intra day]
* Feature Engineering
  * Factors database construction 
  * cancellation is important
  * top k(default 3) largest 
  * aggressive buy and sell, buy MO
* Auto Market Making in pools of the defi
* Motivation of the trading volume prediction
  * Optimal execution: vwap
  * Cancellation alpha
  * Past traded volume
  * Past traded number of orders 
* [How and When are High-Frequency Stock Returns Predictable?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4095405) by Jianqing Fan  
* Create database(SQLite) and webapp based on Flask
