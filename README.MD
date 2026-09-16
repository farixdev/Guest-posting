# Guest Post Backlink Finder

A simple Python automation tool that finds guest posting opportunities for backlink building. It searches for relevant "write for us" / guest post pages based on your target keywords, extracts contact info, and logs everything to a CSV/Excel file for outreach.

## Features

- Searches Google (or a search API) for guest post opportunities using custom footprints (e.g. `"write for us" + keyword`, `"guest post guidelines"`, etc.)
- Filters out duplicate/irrelevant domains
- Extracts contact emails from target pages (where available)
- Checks basic domain metrics (optional, if you plug in an SEO API)
- Exports results to CSV/Excel for tracking outreach
- Simple config file — no code changes needed to run new searches

## Requirements

- Python 3.9+
- Install dependencies:

```bash
pip install -r requirements.txt
```

Typical dependencies used in a tool like this:

```
requests
beautifulsoup4
pandas
selenium          # if scraping JS-heavy search results
python-dotenv      # for API keys / config
openpyxl           # for Excel export
```

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/farixdev/guest-post-finder.git
   cd guest-post-finder
   ```
2. Create a `.env` file for any API keys (e.g. SerpAPI, email finder API):
   ```
   SEARCH_API_KEY=your_key_here
   ```
3. Edit `config.py` (or `config.json`) with your target keywords and footprints:
   ```python
   KEYWORDS = ["digital marketing", "SEO tips"]
   FOOTPRINTS = ['"write for us"', '"guest post guidelines"', '"contribute to us"']
   ```

## Usage

Run the main script:

```bash
python main.py
```

Results will be saved to `output/guest_post_leads.csv` with columns like:

| Domain | Page URL | Contact Email | Keyword Matched | Notes |
|--------|----------|----------------|------------------|-------|

## Project Structure

```
guest-post-finder/
├── main.py              # Entry point
├── config.py            # Keywords, footprints, settings
├── scraper.py           # Search + scraping logic
├── email_extractor.py   # Pulls contact emails from pages
├── exporter.py          # Handles CSV/Excel export
├── output/               # Generated results
└── requirements.txt
```

## Notes

- Respect each search engine's and website's terms of service and `robots.txt` — this tool is meant to speed up manual research, not to spam.
- Rate-limit your requests to avoid getting IP-blocked.
- Always manually vet a site's quality (traffic, relevance, spam score) before pitching or building a link.

## License

MIT
