# CS5720 - Neural Networks and Deep Learning  
### Home Assignment 1 – Summer 2025  
**Student Name:** shreya surakanti
**Student Id:** 700774082
**University of Central Missouri**  
**Course:** CS5720 Neural Networks and Deep Learning  

---

## Assignment Overview

This assignment is divided into three key parts:

1. **Tensor Manipulations & Reshaping**
2. **Loss Functions & Hyperparameter Tuning**
3. **Neural Network Training with TensorBoard**

---

## Part 1: Tensor Manipulations & Reshaping

### Tasks Completed:
- Created a random tensor with shape **(4, 6)** using TensorFlow.
- Found its **rank** and **shape**.
- Reshaped to **(2, 3, 4)** and transposed to **(3, 2, 4)**.
- Broadcasted a tensor of shape **(1, 4)** and added it.
  
### Outputs:
- **Original Shape:** (4, 6)  
- **Rank:** 2  
- **Reshaped Shape:** (2, 3, 4)  
- **Transposed Shape:** (3, 2, 4)

### Broadcasting Explained:
TensorFlow broadcasting automatically expands the smaller tensor to match the shape of the larger one along compatible dimensions. This allows element-wise operations without needing explicit reshaping.

---

## Part 2: Loss Functions & Hyperparameter Tuning

### Tasks Completed:
- Defined sample true labels and model predictions.
- Calculated:
  - **Mean Squared Error (MSE)**
  - **Categorical Cross-Entropy (CCE)**
- Modified predictions and recalculated losses.
- Plotted a bar chart comparing MSE and CCE.

### Results:
| Prediction Version | MSE Loss | CCE Loss |
|--------------------|----------|----------|
| Initial             | 0.0167   | 0.3562   |
| Modified            | 0.0102   | 0.2594   |

### Insight:
- MSE is more sensitive to small numeric differences.
- Cross-Entropy is more appropriate for classification tasks as it penalizes incorrect class probabilities more heavily.

---

## Part 3: Neural Network Training with TensorBoard

### Tasks Completed:
- Loaded and preprocessed the **MNIST** dataset.
- Built a simple neural network model.
- Trained the model for **5 epochs** with **TensorBoard logging**.
- Analyzed training and validation metrics using TensorBoard.

### Model Details:
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam
- **Learning Rate:** 0.001
- **Epochs:** 5
- **Batch Size:** 32

### TensorBoard Log Directory:
logs/fit/20250526-125927/train

yaml
Copy
Edit

### Observations:
- **Training Accuracy:** Improved to **0.9858**
- **Validation Accuracy:** Improved to **0.9773**
- **Training Loss:** Decreased to **0.0461**
- **Validation Loss:** Decreased to **0.074**
- Weight and bias histograms remained within expected distributions.

---

### TensorBoard Questions Answered:

**1. What patterns do you observe in the accuracy curves?**  
Both training and validation accuracies increased smoothly and closely followed each other, indicating good generalization.

**2. How can you detect overfitting using TensorBoard?**  
Overfitting can be detected if training accuracy increases while validation accuracy plateaus or decreases. Similarly, a diverging validation loss is a strong indicator.

**3. What happens if the number of epochs increases?**  
The model may begin to overfit the training data unless regularization is applied. TensorBoard would show training loss decreasing while validation loss increases.

---
## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd home_assignment_1
2. Install Dependencies
Install required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Python Scripts
bash
Copy
Edit
python tensor_ops.py
python loss_functions.py
python mnist_tensorboard.py
4. Launch TensorBoard
Start TensorBoard to visualize training logs:

bash
Copy
Edit
tensorboard --logdir=logs/fit
Then open the browser and go to:

http://localhost:6006
