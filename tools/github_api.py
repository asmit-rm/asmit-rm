import requests

GITHUB_API = "https://api.github.com"


class GitHubAPI:
    def __init__(self, username, token=None):
        self.username = username
        self.session = requests.Session()

        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "asmit-rm-profile-generator"
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        self.session.headers.update(headers)

    def _get(self, endpoint):
        url = f"{GITHUB_API}{endpoint}"
        r = self.session.get(url, timeout=20)
        r.raise_for_status()
        return r.json()

    def profile(self):
        return self._get(f"/users/{self.username}")

    def repositories(self):
        repos = []
        page = 1

        while True:
            data = self._get(
                f"/users/{self.username}/repos?per_page=100&page={page}"
            )

            if not data:
                break

            repos.extend(data)
            page += 1

        return repos

    def stats(self):
        profile = self.profile()
        repos = self.repositories()

        total_stars = sum(r["stargazers_count"] for r in repos)
        total_forks = sum(r["forks_count"] for r in repos)

        languages = {}

        for repo in repos:
            lang = repo.get("language")

            if lang:
                languages[lang] = languages.get(lang, 0) + 1

        return {
            "name": profile.get("name"),
            "login": profile.get("login"),
            "followers": profile.get("followers"),
            "following": profile.get("following"),
            "public_repos": profile.get("public_repos"),
            "avatar": profile.get("avatar_url"),
            "stars": total_stars,
            "forks": total_forks,
            "languages": languages,
        }


if __name__ == "__main__":
    api = GitHubAPI("asmit-rm")
    from pprint import pprint
    pprint(api.stats())
