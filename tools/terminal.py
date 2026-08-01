from tools.config import NAME, ALIAS, GITHUB, TELEGRAM, TAGLINE, THEME

def show_terminal():
    print(f"User: {NAME}")
    print(f"Alias: {ALIAS}")
    print(f"GitHub: {GITHUB}")
    print(f"Telegram: {TELEGRAM}")
    print(f"Tagline: {TAGLINE}")

if __name__ == "__main__":
    show_terminal()
