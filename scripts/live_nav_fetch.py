import requests
import pandas as pd

amfi_codes = [
    119551,
    120503,
    118632,
    119092,
    125497
]

for code in amfi_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    print(f"\nFetching {code}")

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/live_nav_{code}.csv",
        index=False
    )

    print("Saved successfully")