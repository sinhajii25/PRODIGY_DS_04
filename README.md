# PRODIGY_DS_04

This project is a part of my Data Science Internship at **Prodigy InfoTech**.

The objective is to perform **Sentiment Analysis on Twitter data** using the TextBlob library. The tweets are analyzed to classify their sentiment as **Positive**, **Neutral**, or **Negative**, and the results are visualized using Seaborn.

---

## Objective

**Perform sentiment classification** on real-world Twitter data using natural language processing (NLP) techniques.

### This project includes:

- Loading and processing tweet data  
- Performing sentiment analysis using TextBlob  
- Classifying tweets based on polarity  
- Visualizing sentiment distribution

---

## Files Included

| File Name               | Description                                      |
|------------------------|--------------------------------------------------|
| `main.py`              | Python script for data analysis and visualization |
| `twitter_sentiments.csv` | Dataset used for sentiment analysis             |
| `README.md`            | Project documentation                            |

---

## Tools & Libraries Used

- Python 3  
- Pandas  
- TextBlob  
- NLTK  
- Seaborn  
- Matplotlib

---

## Sentiment Analysis Details

- **Library Used**: TextBlob  
- **Polarity Score**: Ranges from -1 (negative) to +1 (positive)  
- **Classification Rule**:
  - Polarity > 0 → Positive  
  - Polarity = 0 → Neutral  
  - Polarity < 0 → Negative

---

## Output Visualization

The project includes a **bar chart** displaying the count of tweets in each sentiment category using Seaborn’s `countplot`.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sinhajii25/PRODIGY_DS_04.git
cd PRODIGY_DS_04

### 2. Install Dependencies

```bash

pip install pandas textblob nltk seaborn matplotlib

### 3. Run the Script

python main.py

---

# Author

Aditya Sinha
B.Tech – Artificial Intelligence & Data Science
Dr. Akhilesh Das Gupta Institute of Professional Studies

LinkedIn: www.linkedin.com/in/adityasinha25

