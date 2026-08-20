import os
import shutil
from pathlib import Path

def get_chrome_cache():
    home = Path.home()

    if os.name == "nt":  # Windows
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/User Data/Default/Cache"

    elif os.name == "posix":
        if Path("/Applications/Google Chrome.app").exists():  # macOS
            return home / "Library/Caches/Google/Chrome/Default"

        # Linux
        return home / ".cache/google-chrome/Default"

    return None


def clear_chrome_cache():
    cache = get_chrome_cache()

    if not cache or not cache.exists():
        print("Chrome cache folder was not found.")
        return

    removed = 0

    for item in cache.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

            removed += 1
        except OSError:
            pass

    print(f"Chrome cache cleared. Removed {removed} items.")


if __name__ == "__main__":
    clear_chrome_cache()
