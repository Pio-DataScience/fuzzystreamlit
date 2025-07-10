# Fuzzy String Similarity Comparison

A Streamlit web application that compares two text strings using various fuzzy matching algorithms from the RapidFuzz library.

## Features

- Token Sort Ratio comparison
- Token Set Ratio comparison
- Levenshtein Distance calculation
- Indel Distance calculation
- Detailed breakdown of Token Sort Ratio calculation

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd fuzzy_streamlit
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser. Enter two text strings and click "Compare" to see various similarity metrics and a detailed breakdown of the comparison process.

## Dependencies

- Python 3.6+
- streamlit==1.39.0
- rapidfuzz==3.10.0

## License

This project is open source and available under the MIT License. 