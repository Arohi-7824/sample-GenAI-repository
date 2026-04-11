import matplotlib.pyplot as plt
import numpy as np

print("Creating training Visualizations...")
epochs=np.arange(1,11)

train_loss=1.0/np.sqrt(epochs)
val_loss=1.0/np.sqrt(epochs)+0.1

plt.figure(figsize=(10,6))

plt.plot(epochs,train_loss,'b--',label='Training loss',marker='o')
plt.plot(epochs,val_loss,'r--',label='Validation Loss',marker='s')

plt.xlabel('Epoch',fontsize=12)
plt.ylabel('Loss',fontsize=12)
plt.title('Model Training Program',fontsize=12,fontweight='bold')
plt.legend()

plt.grid(True,alpha=0.3)

plt.savefig('training_progress.png',dpi=150,bbox_inches='tight')

print("Saved Training_progress.png")

plt.show()
#End of loss plot


#accuracy plot
plt.figure(figsize=(10,6))
train_acc=1-(1/(epochs+1))

val_acc=train_acc-0.5

plt.plot(epochs,train_acc,'g--',label='Training Accuracy',marker='o')
plt.plot(epochs,val_acc,'orange',label='Validation Accuracy',marker='s',linestyle='--')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Time')
plt.legend()
plt.grid(True,alpha=0.2)

plt.savefig('accuracy_progress.png',dpi=150,bbox_inches='tight')
print('Saved accuracy_progress.png')

plt.show()