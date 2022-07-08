from scipy.io import loadmat
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import random
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load the Letters subset, then transform the loaded data into a format usable for use with scikit-learn.
data = {}
loadmat("matlab/emnist-letters.mat", mdict = data)
letters = data["dataset"][0, 0] # Assign the dataset to another variable; 
# [0, 0] after keywords strip off extraneous nested arrays

# Assign the training, testing, and mapping dictionaries each to their own variables
train = letters["train"][0, 0] # See comment on line 12
test = letters["test"][0, 0]
mapping = letters["mapping"] # Mapping list is final

# Separate the training and testing sets intomapp images and labels
X_train = train["images"]
y_train = np.ravel(train["labels"])
X_test = test["images"]
y_test = np.ravel(test["labels"])

# Visualize the first 50 training samples in a 5x10 grid (section 15.2.3). 
#   Convert each row of 784 features into a 2D array of 28 x 28 data points.
make_square = lambda x: np.reshape(x, (28, 28))
display = [make_square(n) for n in X_train[:50]]

#   Each letter needs to be rotated 90° clockwise and mirrored:
display = [np.flip(np.rot90(m, k = 1, axes = (0, 1)), axis = 0) for m in display]

#   Create a labels_text list of the same size which contains the matching uppercase letters.
make_char = lambda x: chr(mapping[x][1])
labels_text = [make_char(x - 1) for x in y_train[:50]]

#   Set up and display the visualization
figure_1, axes_1 = plt.subplots(nrows = 5, ncols = 10, figsize = (10, 5))
for item in zip(axes_1.ravel(), display, labels_text):
    axes_1, image, target = item
    axes_1.imshow(image, cmap=plt.cm.gray_r)
    axes_1.set_xticks([]) # Remove x-axis tick marks
    axes_1.set_yticks([]) # Remove y-axis tick marks
    axes_1.set_title(target)
plt.tight_layout()
plt.show()

# Create and train the model
knn = KNeighborsClassifier()
knn.fit(X = X_train, y = y_train)

# Apply the model to the test dataset to make predictions
predicted = knn.predict(X = X_test)
expected = y_test

# Calculate and display the prediction accuracy percentage.
#   Keep track of the image for the next step
wrong = [(i, p, e) for (i, p, e) in zip(X_test, predicted, expected) if p != e]
print(f"Prediction accuracy: {(len(expected) - len(wrong)) / len(expected):.2%}")

# Use sample to create a 50-element dataframe out of the misclassified values.
wrong_images = pd.DataFrame(random.sample(wrong, k = 50), columns = ["Image", "Predicted", "Expected"])

# Visualize the sample
wrong_images["Image"] = [make_square(i) for i in wrong_images["Image"]]
wrong_images["Image"] = [np.flip(np.rot90(m, k = 1, axes = (0, 1)), axis = 0) for m in wrong_images["Image"]]
wrong_images["Predicted"] = [make_char(p - 1) for p in wrong_images["Predicted"]]
figure_2, axes_2 = plt.subplots(nrows = 5, ncols = 10, figsize = (10, 5))
for item in zip(axes_2.ravel(), wrong_images["Image"], wrong_images["Predicted"]):
    axes_2, image, target = item
    axes_2.imshow(image, cmap=plt.cm.gray_r)
    axes_2.set_xticks([]) # Remove x-axis tick marks
    axes_2.set_yticks([]) # Remove y-axis tick marks
    axes_2.set_title(target)
plt.tight_layout()
plt.show()

# Create a classification report (section 15.3.1) and print the letters with the 
#   lowest & highest precision, and the letters with the lowest/highest recall.
# Hint: use the flag to return the report as a Dictionary, then convert to DataFrame.
names = [make_char(x) for x in range(26)]
report = pd.DataFrame(classification_report(expected, predicted, target_names = names, output_dict = True))
precision_sort = report.loc["precision"].sort_values()
min_precision = precision_sort.index[0]
max_precision = precision_sort.index[-1]
recall_sort = report.loc["recall"].sort_values()
min_recall = recall_sort.index[0]
max_recall = recall_sort.index[-1]
print(f"Highest precision: {max_precision}\nLowest precision: {min_precision}")
print(f"Highest recall: {max_recall}\nLowest recall: {min_recall}")