import streamlit as st
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Emotion Classifier",
    page_icon="😊",
    layout="wide"
)

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('emotion_classify_model.pkl')


# Main app
def main():
    # Header
    st.title("🎭 Emotion Classification System")
    st.markdown("**Classify emotions in text using AI/ML - Built with TF-IDF & Random Forest**")
    st.markdown("---")
    
    # Sidebar with project info
    st.sidebar.header("📊 Project Details")
    st.sidebar.info("""
    **Model Performance:**
    - Accuracy: 94%
    - Cross-validation: 91.7% (±2.1%)
    - Dataset: 5,937 text samples
    - Features: TF-IDF vectorization
    - Algorithm: Random Forest
    """)
    
    st.sidebar.header("🎯 Emotions Detected")
    st.sidebar.success("😂 **Joy** - Positive, happy emotions")
    st.sidebar.warning("😨 **Fear** - Anxious, worried emotions") 
    st.sidebar.error("😡 **Anger** - Frustrated, angry emotions")
    
    # Load model
    try:
        model = load_model()
        st.success("✅ Model loaded successfully!")
    except:
        st.error("❌ Error loading model. Please check if 'emotion_classify_model.pkl' exists.")
        return
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🔍 Classify Your Text")
        
        # Text input options
        input_method = st.radio("Choose input method:", 
                               ["Type your text", "Try example texts"])
        
        if input_method == "Type your text":
            user_input = st.text_area("Enter text to analyze:", 
                                    placeholder="Type your message here...",
                                    height=120)
        else:
            example_texts = {
                "Joyful": "I'm so excited about my new job! This is the best day ever!",
                "Fearful": "I am scared of the dark.",
                "Angry": "I'm so frustrated with this terrible customer service!"
            }
            
            selected_example = st.selectbox("Select example:", list(example_texts.keys()))
            user_input = st.text_area("Example text:", 
                                    value=example_texts[selected_example],
                                    height=120)
        
        # Predict button
        if st.button("🚀 Analyze Emotion", type="primary"):
            if user_input.strip():
                # Make prediction
                prediction = model.predict([user_input])[0]
                probabilities = model.predict_proba([user_input])[0]
                
                # Emotion mapping
                emotion_map = {0: "Joy 😂", 1: "Fear 😨", 2: "Anger 😡"}
                predicted_emotion = emotion_map[prediction]
                
                # Display results
                st.markdown("### 📈 Results")
                
                # Main prediction
                if prediction == 0:  # Joy
                    st.success(f"**Predicted Emotion: {predicted_emotion}**")
                elif prediction == 1:  # Fear
                    st.warning(f"**Predicted Emotion: {predicted_emotion}**")
                else:  # Anger
                    st.error(f"**Predicted Emotion: {predicted_emotion}**")
                
                # Confidence scores
                st.markdown("### 🎯 Confidence Scores")
                
                # Create probability dataframe
                prob_df = pd.DataFrame({
                    'Emotion': ['Joy 😂', 'Fear 😨', 'Anger 😡'],
                    'Probability': probabilities,
                    'Percentage': [f"{p:.1%}" for p in probabilities]
                })
                
                # Horizontal bar chart
                fig = px.bar(prob_df, x='Probability', y='Emotion', 
                           orientation='h',
                           color='Probability',
                           color_continuous_scale='viridis',
                           title="Confidence Scores by Emotion")
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
                
                # Confidence interpretation
                max_confidence = max(probabilities)
                if max_confidence > 0.8:
                    st.success(f"🎯 High confidence prediction ({max_confidence:.1%})")
                elif max_confidence > 0.6:
                    st.info(f"🤔 Medium confidence prediction ({max_confidence:.1%})")
                else:
                    st.warning(f"⚠️ Low confidence prediction ({max_confidence:.1%})")
            else:
                st.error("Please enter some text to analyze!")
    
    with col2:
        st.header("📚 How It Works")
        st.markdown("""
        **1. Text Preprocessing**
        - Remove stop words & punctuation  
        - Lemmatization using spaCy
        
        **2. Feature Extraction**
        - TF-IDF vectorization
        - Unigrams + Bigrams (1,2)
        
        **3. Classification**
        - Random Forest algorithm
        - Trained on 5,937 samples
        
        **4. Results**
        - Emotion prediction
        - Confidence scores
        """)
        
        st.header("🏆 Model Performance")
        
        # Performance metrics
        metrics_data = {
            'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
            'Joy': ['94%', '94%', '95%', '95%'],
            'Fear': ['94%', '92%', '94%', '93%'],
            'Anger': ['94%', '94%', '91%', '93%']
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, hide_index=True)

# Footer
def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Created by Sankaran S
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_footer()
