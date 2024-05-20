import requests
from bs4 import BeautifulSoup
from git import Repo

# Function to fetch updated links from a website
def fetch_updated_links():
    # Example: Scraping links from a website
    response = requests.get('https://example.com/updated_links')
    soup = BeautifulSoup(response.text, 'html.parser')
    # Parse the page and extract new links
    updated_links = [link['href'] for link in soup.find_all('a')]
    return updated_links

# Function to remove expired links from the M3U playlist
def remove_expired_links(m3u_file, expired_links):
    with open(m3u_file, 'r') as file:
        lines = file.readlines()
    # Filter out expired links
    updated_lines = [line for line in lines if not any(expired_link in line for expired_link in expired_links)]
    # Write updated lines back to the file
    with open(m3u_file, 'w') as file:
        file.writelines(updated_lines)

# Update M3U playlist
def update_m3u_playlist():
    # Fetch updated links
    updated_links = fetch_updated_links()
    # Remove expired links
    remove_expired_links('playlist.m3u', ['expired_link1', 'expired_link2'])  # Replace with actual expired links
    # Append new links to the M3U file
    with open('playlist.m3u', 'a') as file:
        for link in updated_links:
            file.write(f'{link}\n')

    # Commit changes to GitHub repository
    repo = Repo('/path/to/your/repository')
    repo.git.add('playlist.m3u')
    repo.git.commit('-m', 'Updated playlist')
    repo.git.push()

# Run the update process
update_m3u_playlist()
