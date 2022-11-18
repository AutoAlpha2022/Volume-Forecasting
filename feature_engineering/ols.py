# -*- coding: utf-8 -*-

import pandas as pd
from data_processing.data_pipeline import get_data, feature_overlap, feature_disjoint
from feature_engineering.utils import data_split



def ols(train, test):
    def out_of_sample(results, test):
        pred_x = test[0]
        pred_x = sm.add_constant(pred_x, has_constant='add')
        pred_y = results.predict(pred_x)
        real_y = test[1]
        from sklearn.metrics import mean_squared_error, r2_score
        r_squared = r2_score(real_y,pred_y)  
        return r_squared
    import statsmodels.api as sm
    X = train[0]
    X = sm.add_constant(X)
    Y = train[1]
    results = sm.OLS(Y,X).fit()
    print(results.summary())
    return out_of_sample(results, test)
  
if __name__ == "__main__":
    # data,_ = get_data()
    # data = feature_overlap()
    data = feature_disjoint()
    train, test = data_split(data,size = 10)
    out_of_sample = ols(train, test)
    print(f">>> out_of_sample: {out_of_sample}")

















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    