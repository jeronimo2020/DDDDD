from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluador_modelo(model, X_test, y_test):
    print("Evaluando el rendimiento del modelo...")
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"MAE: {mae}, MSE: {mse}")
    print("Rendimiento del modelo evaluado")
    return mae, mse

def metricas_especializadas(y_test, y_pred):
    print("Calculando métricas especializadas para evaluar el modelo...")
    from sklearn.metrics import r2_score
    r2 = r2_score(y_test, y_pred)
    print(f"R2 Score: {r2}")
    print("Métricas especializadas calculadas")

def generador_reportes(history):
    print("Generando reportes detallados sobre el rendimiento del modelo...")
    import pandas as pd
    report = pd.DataFrame(history.history)
    report.to_csv('training_report.csv', index=False)
    print("Reportes detallados generados")

def validador_cruzado(model, X, y, folds=5):
    print("Realizando validación cruzada del modelo...")
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=folds)
    for train_index, val_index in kf.split(X):
        X_train, X_val = X[train_index], X[val_index]
        y_train, y_val = y[train_index], y[val_index]
        model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)
    print("Validación cruzada del modelo realizada")

def analizador_resultados(y_test, y_pred):
    print("Analizando los resultados del modelo...")
    import matplotlib.pyplot as plt
    plt.scatter(y_test, y_pred)
    plt.xlabel('Valores Reales')
    plt.ylabel('Predicciones')
    plt.show()
    print("Resultados del modelo analizados")

def analizador_datos(datos):
    print("Analizando los datos utilizados para el entrenamiento y validación...")
    import pandas as pd
    data_summary = pd.DataFrame(datos).describe()
    print(data_summary)
    print("Datos utilizados para el entrenamiento y validación analizados")
