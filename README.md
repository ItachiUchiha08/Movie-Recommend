# 🎬 Movie Recommend

## 📌 Overview
The **Movie Recommendation System** is a content-based filtering application that suggests movies to users based on their preferences. It utilizes the **TMDB 5000 Movies Dataset** from Kaggle and provides an interactive frontend built with **Streamlit**.

## ⭐ Features
- 🎭 Content-based filtering using **TF-IDF Vectorization**.
- 📊 Similarity computation using **Cosine Similarity**.
- 🎨 Interactive and user-friendly **Streamlit** interface.
- 🔍 Movie search functionality.
- 🖼️ Displays recommended movie posters and details.

## 📂 Dataset
The project uses the **TMDB 5000 Movies Dataset**, available on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). The dataset includes:
- 🎬 Movie titles
- 📖 Overview (plot summary)
- 🎭 Genres
- 🎥 Cast & Crew
- 🔑 Keywords and tags

## ⚙️ Installation
### 📌 Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### 🚀 Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 🎥 Usage
1. Open the **Streamlit UI** in your browser.
2. 🔎 Search for a movie in the input field.
3. 🤖 The system will return a list of recommended movies based on content similarity.
4. 🖼️ View movie posters and details alongside recommendations.


## 🛠️ Technologies Used
- 🐍 **Python**
- 🏗️ **Pandas & NumPy** for data processing
- 📊 **Scikit-learn** for vectorization and similarity calculations
- 🌐 **Streamlit** for frontend
- 🔗 **Requests** for fetching additional movie data

## 🚀 Future Enhancements
- 🔄 Hybrid filtering (combining collaborative & content-based)
- 👤 Personalized user profiles
- 🏆 Integration with a movie database API for real-time updates

## 📜 Credits
Dataset sourced from **Kaggle (TMDB 5000 Movies Dataset)**

## 📝 License
This project is licensed under the MIT License.

