"""
Plots confusion matrix & precision-recall
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

class ModelEvaluator:
    @staticmethod
    def evaluate(y_true, y_pred):
        print("Classification Report:")
        print(classification_report(y_true,y_pred))

        #Confusion Matrix
        plt.figure(figsize=(6,5))
        sns.heatmap(confusion_matrix(y_true,y_pred), annot=True, fmt='d', cmap="Blues", xticklabels=["A", "B", "C", "D"], yticklabels=["A", "B", "C", "D"])
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        plt.show()