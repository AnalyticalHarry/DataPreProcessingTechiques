def match_feature_target_size(X, y):
    X_shape = X.shape[0]
    y_shape = y.shape[0]
    if X_shape > y_shape:
        return X[:y_shape], y
    elif y_shape > X_shape:
        return X, y[:X_shape]
    else:
        return X, y

X, y = match_feature_target_size(X, y)

## Author : Hemant Thapa
## Date pushed in Github: 20.02.2024
## Programming Language: Python 
