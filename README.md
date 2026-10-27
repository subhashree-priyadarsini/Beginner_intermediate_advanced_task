# DistilBERT Sentiment Analysis

## Project Overview
This project uses a pretrained DistilBERT model to classify English text sentiment as Positive or Negative.

## Technologies Used
- Python
- Jupyter Notebook
- Hugging Face Transformers
- PyTorch
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- SST-2 validation dataset

## Project Workflow
1. Load the pretrained DistilBERT sentiment model.
2. Test the model on sample sentences.
3. Evaluate 200 examples from the SST-2 validation dataset.
4. Calculate accuracy, precision, recall, and F1-score.
5. Visualize the evaluation results.
6. Analyze incorrect predictions and model limitations.

## Evaluation
The model was evaluated on 200 examples. It correctly classified 182 examples and incorrectly classified 18, giving 91% accuracy on this sample.

## Limitations
The model may struggle with sarcasm, mixed sentiment, ambiguous text, and domain-specific language.

## Files
- `sentiment_analysis.ipynb` — Main implementation
- `evaluation_results.csv` — Individual predictions
- `evaluation_metrics.csv` — Evaluation metrics
- `confusion_matrix.csv` — Confusion matrix values
- `confusion_matrix.png` — Confusion matrix visualization
- `exploration_results.csv` — Sample experiment results

## Conclusion
This project demonstrates pretrained transformer-based sentiment analysis and evaluates its performance using metrics, visualizations, and error analysis.