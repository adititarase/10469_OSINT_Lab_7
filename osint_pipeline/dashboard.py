import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

# Set a reliable database path
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "data" / "osint_data.db"

def load_data(db_path):
    """Load data from SQLite database into a pandas DataFrame"""
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM social_media_posts", conn)
        conn.close()
        return df
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

def main():
    st.title("OSINT Dashboard")
    st.write("View and search through collected social media data.")

    # Load data
    df = load_data(DB_PATH)
    if df.empty:
        st.warning("No data found in the database. Run the pipeline first.")
        return

    # Search functionality
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("Search term (case-insensitive):", "")
    with col2:
        search_field = st.selectbox("Search in field:", ["text", "platform", "user", "sentiment", "url"])

    if search_term:
        if search_field in df.columns:
            df_filtered = df[df[search_field].astype(str).str.contains(search_term, case=False, na=False)]
        else:
            st.error(f"Field '{search_field}' not found in data.")
            df_filtered = df
    else:
        df_filtered = df

    # Display data
    st.write(f"Showing {len(df_filtered)} records:")
    st.dataframe(df_filtered)

if __name__ == "__main__":
    main()
