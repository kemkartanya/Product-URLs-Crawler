# Product-URLs-Crawler

## How It Works
The spider starts with the URLs in start_urls.

It extracts product URLs from these pages based on the defined pattern.

For each page, it yields the product URLs and follows all links (pagination) recursively, repeating the process on subsequent pages.
