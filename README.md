
# 🌐 Leadership Profile Scraper

A full-stack web application designed to scrape and display the leadership team profiles (Name, Designation, and Image) from any public corporate "About Us" or "Leadership" webpage.

This project uses a high-performance FastAPI backend for web scraping and a simple, dynamic HTML/CSS/JavaScript frontend to visualize the results.
## ✨ Features

    URL-Agnostic Scraping: Accepts any corporate URL (e.g., Walmart, Mahindra, Google Cloud).

    Dual Scraping Methods: Attempts initial request scraping (requests) and falls back to JavaScript rendering (requests-html with Pyppeteer) if dynamic content is detected.

    Intelligent Extraction: Uses heuristics, keyword matching (e.g., 'CEO', 'President', 'Officer'), and image URL pattern matching to reliably extract profile data.

    FastAPI Backend: Provides a robust, asynchronous API endpoint for the front-end application.

    CORS Enabled: Configured for cross-origin resource sharing for easy local development.

## 🛠️ Tech Stack
### Backend (Python)

    Framework: FastAPI (ASGI)

    Scraping: requests-html, BeautifulSoup4, lxml

    Data Processing: pandas, numpy

### Frontend (Web)

    Language: JavaScript (ES6+), HTML5, CSS

    Interaction: Fetch API for asynchronous communication with the backend.

# Python Notebook is provided in /data_notebook/scrape_website.ipynb

### This is Backend hosted in Render. Reload to avoid cold starts from the cloud
