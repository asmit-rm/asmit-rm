from tools.config import NAME, ALIAS, ROLE, THEME

def generate_banner():
    print(f"{'='*50}")
    print(f"  {NAME} ({ALIAS})")
    print(f"  {ROLE}")
    print(f"{'='*50}")

if __name__ == "__main__":
    generate_banner()
