# -*- coding: utf-8 -*-
"""Upload GitHub profile avatar and repository social preview."""
import json
import subprocess
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

REPO = "BiryukovSergey/CyberLeak-GTA6-Playable-Build-Download"
ROOT = Path(__file__).parent
AVATAR = ROOT / "images" / "github-profile-avatar.jpg"
PREVIEW = ROOT / "images" / "github-social-preview.jpg"


def token() -> str:
    return subprocess.check_output(["gh", "auth", "token"], text=True).strip()


def upload_profile_avatar(t: str) -> bool:
    print("Uploading profile avatar...")
    with AVATAR.open("rb") as f:
        r = requests.post(
            "https://github.com/settings/profile_images/upload",
            headers={"Authorization": f"token {t}", "Accept": "application/json"},
            files={"file": ("avatar.jpg", f, "image/jpeg")},
            timeout=120,
        )
    print("Profile avatar HTTP:", r.status_code)
    if r.ok:
        try:
            data = r.json()
            print("Profile avatar URL:", data.get("avatar_url") or data)
        except Exception:
            print(r.text[:300])
        return True
    print(r.text[:500])
    return False


def upload_social_preview(t: str) -> bool:
    print("Uploading repository social preview...")
    owner, repo = REPO.split("/")
    with PREVIEW.open("rb") as f:
        r = requests.post(
            f"https://github.com/{owner}/{repo}/settings/preview_images/upload",
            headers={"Authorization": f"token {t}", "Accept": "application/json"},
            files={"file": ("social-preview.jpg", f, "image/jpeg")},
            timeout=120,
        )
    print("Social preview HTTP:", r.status_code)
    if r.ok:
        print(r.text[:500])
        return True
    print(r.text[:500])

    # fallback endpoint used by GitHub UI
    with PREVIEW.open("rb") as f:
        r2 = requests.post(
            "https://uploads.github.com/repository-images",
            headers={"Authorization": f"token {t}", "Accept": "application/json"},
            files={"file": ("social-preview.jpg", f, "image/jpeg")},
            data={"owner": owner, "repo": repo},
            timeout=120,
        )
    print("Fallback social preview HTTP:", r2.status_code)
    print(r2.text[:500])
    return r2.ok


def main() -> int:
    if not AVATAR.exists() or not PREVIEW.exists():
        print("Missing image files")
        return 1
    t = token()
    ok1 = upload_profile_avatar(t)
    ok2 = upload_social_preview(t)
    return 0 if ok1 and ok2 else 2


if __name__ == "__main__":
    raise SystemExit(main())
