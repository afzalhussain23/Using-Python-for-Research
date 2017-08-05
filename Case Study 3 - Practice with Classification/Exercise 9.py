predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes[training_indices], k=5) for p in predictors[selection]]

percentage = accuracy(my_predictions, data.high_quality[selection])
print(percentage)