correct_predictions=850
total_predictions=1000

accuracy=(correct_predictions/total_predictions)*100
print("The accuracy of the model is:", accuracy, "%")

target_accuracy=0.90
current_accuracy=0.87
if current_accuracy >= target_accuracy:
    print("The model has achieved the target accuracy.")
else:
    print(f"Need {target_accuracy - current_accuracy:.2%} more accuracy to reach the target.")

dataset_size=50000
task_type="text generation"

if task_type=="classification" and dataset_size <10000:
    model="logistic regression"
    print("Using classification dataset.")
elif task_type=="classification" and dataset_size >=10000:
    model="Neural Network"
    print("Using deep learning model for large classification dataset.")
elif task_type=="text generation":
    model="GPT based transformer"
    print("Using GPT based transformer for text generation.")
else:
    model="Custom model"
    print("Building custom architecture")

print("Selected model:", model)