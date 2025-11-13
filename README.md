# OSINT Pipeline

This project is an Open-Source Intelligence (OSINT) pipeline that collects data from various social media platforms, processes it, and provides a dashboard for viewing and searching the data.

## Features

- **Data Collection**: Fetches posts from multiple platforms including Twitter, Reddit, Facebook, Instagram, TikTok, LinkedIn, Telegram, Mastodon, GitHub, Quora, HackerNews, VK, and Snapchat.
- **Data Processing**: Cleans text, filters for English content, and adds sentiment analysis.
- **Database Storage**: Stores processed data in a SQLite database.
- **Terminal Interface**: Command-line interface for running the pipeline and basic searching.
- **Web Dashboard**: Streamlit-based dashboard for viewing and searching data interactively.

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables (if needed for API keys):
   Create a `.env` file in the root directory and add your API keys.

## Usage

### Running the Pipeline

To collect and process data:

```
python main.py
```

This will fetch data from various platforms, process it, and store it in the database.

### Viewing Data in Terminal

The script prints the latest records in a table format and allows interactive searching.

### Web Dashboard

To launch the interactive dashboard:

```
python -m streamlit run dashboard.py
```

Open your browser to `http://localhost:8501` to view and search the data.

## Project Structure

- `main.py`: Main script for running the OSINT pipeline
- `dashboard.py`: Streamlit dashboard for data visualization and search
- `collectors/`: Modules for collecting data from different platforms
- `utils/`: Utility modules for data cleaning, database operations, and sentiment analysis
- `data/`: Directory for storing the SQLite database
- `requirements.txt`: Python dependencies


