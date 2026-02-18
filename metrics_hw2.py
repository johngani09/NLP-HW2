import numpy as np

confusion = np.array([
    [5,10,5],
    [15,20,10],
    [0,15,10]
])

labels = ["Cat","Dog","Rabbit"]

precisions = []
recalls = []

for i,label in enumerate(labels):
    tp = confusion[i,i]
    fp = confusion[:,i].sum() - tp
    fn = confusion[i,:].sum() - tp

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)

    precisions.append(precision)
    recalls.append(recall)

    print(f"{label} Precision: {precision:.3f}")
    print(f"{label} Recall: {recall:.3f}\n")

print("Macro Precision:", np.mean(precisions))
print("Macro Recall:", np.mean(recalls))

total_correct = np.trace(confusion)
total = confusion.sum()

print("Micro Precision:", total_correct/total)
print("Micro Recall:", total_correct/total)
