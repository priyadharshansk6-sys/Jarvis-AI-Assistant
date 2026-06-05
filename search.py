from ddgs import DDGS
import requests

def search_web(query, max_results=5):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "No results found."
        summary = ""
        for r in results:
            summary += f"{r['title']}: {r['body']}\n\n"
        return summary
    except Exception as e:
        return f"Search failed: {str(e)}"

def get_weather(city="Chennai"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        return response.text
    except:
        return search_web(f"weather in {city} today")

if __name__ == "__main__":
    print(search_web("latest AI news"))