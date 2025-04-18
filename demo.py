import requests

def fetch_cache_usage():
    url = "https://api.github.com/orgs/https-github-com-Gousiya-SNP/actions/cache/usage-by-repository"
    response = requests.get(url)
    data = response.json()
    
    if "total_count" in data:
        if data["total_count"] == 0:
            print("No cache usage found.")
        else:
            for repo in data["repository_cache_usages"]:
                print(f"Repository: {repo['repository']['name']}")
                print(f"Cache Size: {repo['cache_size_in_bytes']} bytes")
                print(f"Cache Count: {repo['cache_count']}")
                print("-----")
    else:
        print("Unexpected response format:", data)

if __name__ == "__main__":
    fetch_cache_usage()
