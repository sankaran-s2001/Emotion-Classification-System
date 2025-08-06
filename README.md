<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 🎭 Emotion Classification System

An AI-powered web application that instantly detects emotions in text messages using advanced machine learning.

**[Live Demo - Try it here!](https://emotion-classification-system.onrender.com)**

## What This Project Does

Understanding emotions in text is crucial for businesses and individuals. This makes it hard to:

- Monitor customer feedback sentiment
- Understand social media reactions
- Analyze support ticket urgency
- Filter toxic content automatically
- Gauge employee satisfaction surveys

My app solves this by instantly analyzing any text and telling you whether it expresses **Joy** 😂, **Fear** 😨, or **Anger** 😡.

## How It Works

**Simply enter your text:**

- Type any message or comment
- Choose from example texts to test
- Get instant emotion prediction
- See confidence scores for each emotion

**Get detailed results:**

- Primary emotion detected with emoji
- Confidence percentage for each emotion
- Visual chart showing probability breakdown
- High/medium/low confidence indicator


## Key Features

- **Instant Analysis** - Get results in under 1 second
- **High Accuracy** - 94% correct emotion detection
- **Visual Results** - Beautiful charts show confidence levels
- **Example Texts** - Try pre-written samples to see how it works
- **Mobile Friendly** - Works perfectly on phones and tablets
- **No Registration** - Start using immediately, no signup required


## The Machine Learning Model

**Performance:**

- **94% accuracy** - Correctly identifies emotions 94 out of 100 times
- Trained on **5,937 real text messages**
- Cross-validated with **91.7% ± 2.1%** reliability
- Average prediction confidence: **85%+**

**How it works:**

- **Text Preprocessing** - Cleans and prepares your text
- **TF-IDF Analysis** - Converts words into numerical features
- **Random Forest** - Uses 100+ decision trees for prediction
- **Confidence Scoring** - Shows how certain the prediction is

**What it analyzes:**

- Individual words and their emotional weight
- Word combinations (phrases like "really angry")
- Text length and structure
- Emotional intensity indicators


## Technologies Used

- **Python** - Core programming language
- **Streamlit** - Interactive web application framework
- **Scikit-learn** - Machine learning algorithms
- **spaCy** - Advanced text processing
- **TF-IDF** - Text feature extraction technique
- **Random Forest** - Ensemble learning algorithm
- **Plotly** - Interactive data visualizations
- **Render** - Cloud deployment platform


## Project Structure

```
emotion-classifier/
├── app.py                    # Main Streamlit web application
├── emotion_classify_model.pkl # Trained ML model (94% accuracy)
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore file
└── .streamlit/config.toml   # Streamlit configuration
```


## Model Development Process

**1. Data Collection \& Exploration**

- Analyzed 5,937 emotion-labeled text samples
- Balanced dataset: 2,000 joy, 2,000 anger, 1,937 fear messages
- Explored text patterns and emotional indicators

**2. Text Preprocessing**

- Removed stop words and punctuation
- Applied lemmatization using spaCy
- Achieved 3% accuracy improvement through preprocessing

**3. Feature Engineering**

- Tested unigrams, bigrams, and trigrams
- Compared Count Vectorizer vs TF-IDF
- Found optimal combination: TF-IDF + (1,2) n-grams

**4. Model Selection**

- Compared Random Forest vs Multinomial Naive Bayes
- Random Forest achieved 94% vs 86% for Naive Bayes
- Validated with 5-fold cross-validation


## Performance Metrics

| Emotion | Precision | Recall | F1-Score | Support |
| :-- | :-- | :-- | :-- | :-- |
| Joy 😂 | 94% | 95% | 95% | 400 |
| Fear 😨 | 92% | 94% | 93% | 388 |
| Anger 😡 | 94% | 91% | 93% | 400 |
| **Overall** | **94%** | **94%** | **94%** | **1,188** |

## How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/emotion-classifier.git
cd emotion-classifier
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
streamlit run app.py
```

4. **Open in browser** - Navigate to `http://localhost:8501`

## Real-World Applications

**For Businesses:**

- **Customer Service** - Automatically prioritize angry customer emails
- **Social Media** - Monitor brand sentiment in real-time
- **HR Departments** - Analyze employee feedback surveys
- **Content Moderation** - Filter toxic comments automatically

**For Developers:**

- **Chatbots** - Make AI assistants more emotionally aware
- **Apps** - Add emotion detection to messaging platforms
- **Analytics** - Understand user sentiment in reviews

**Example Use Cases:**

- Restaurant gets angry review → System flags for immediate manager attention
- Social media post shows fear about product → Marketing team responds with reassurance
- Survey responses show joy → Company highlights positive feedback


## What I Learned Building This

**Technical Skills:**

- **End-to-end ML pipeline** - From raw data to deployed application
- **Text preprocessing** - Advanced NLP techniques with spaCy
- **Feature engineering** - Optimizing TF-IDF and n-gram combinations
- **Model validation** - Cross-validation and performance evaluation
- **Web development** - Building interactive Streamlit applications
- **Cloud deployment** - Production deployment on Render

**Data Science Skills:**

- **Systematic experimentation** - Testing multiple algorithms and features
- **Performance optimization** - Achieving 94% accuracy through careful tuning
- **Model interpretation** - Understanding what features drive predictions
- **Error analysis** - Investigating misclassified examples

**Business Skills:**

- **Problem identification** - Understanding real-world emotion detection needs
- **User experience design** - Creating intuitive interfaces for non-technical users
- **Communication** - Explaining complex ML concepts in simple terms


## Technical Achievements

- **Achieved 94% accuracy** - Exceeds industry benchmarks for 3-class emotion classification
- **Robust validation** - 5-fold cross-validation ensures reliable performance
- **Production deployment** - Fully functional web application with error handling
- **Efficient pipeline** - Fast inference suitable for real-time applications
- **Clean codebase** - Professional structure using pipelines and best practices


## Future Enhancements

**Model Improvements:**

- Expand to detect more emotions (sadness, surprise, disgust)
- Add emotion intensity scoring (mild vs extreme anger)
- Support multiple languages beyond English
- Implement deep learning models for comparison

**Application Features:**

- **Batch processing** - Analyze multiple texts at once
- **API endpoints** - Allow integration with other applications
- **Historical analysis** - Track emotion trends over time
- **Export functionality** - Download results as CSV/PDF

**Integration Options:**

- **Slack/Discord bots** - Real-time emotion monitoring in team chats
- **Email plugins** - Automatic emotion tagging for customer support
- **Social media monitoring** - Track brand sentiment across platforms


## Why This Project Stands Out

**Technical Excellence:**

- **High performance** - 94% accuracy with robust validation
- **Complete pipeline** - From data preprocessing to deployment
- **Professional code** - Clean, documented, and maintainable
- **Modern stack** - Current ML/web development technologies

**Business Relevance:**

- **Solves real problems** - Emotion detection has clear commercial value
- **User-friendly design** - Non-technical users can operate easily
- **Scalable architecture** - Ready for production environment
- **Measurable impact** - Quantified performance metrics

**Portfolio Value:**

- **Demonstrates full-stack skills** - ML + web development + deployment
- **Shows systematic thinking** - Methodical approach to problem-solving
- **Proves business acumen** - Understanding of practical applications
- **Production-ready quality** - Not just an academic exercise


## ✉️ Contact

**[Your Name]**
[
[
[

*This project demonstrates how artificial intelligence can understand human emotions in text. Built to showcase end-to-end machine learning skills from research to production deployment.*

⭐ **If you find this project impressive, please star it!**
