import requests
import json
import time
import os
from datetime import date
from typing import Optional, Dict, Any

class StravaClient:
    def __init__(self, access_token: str):
        self.base_url = "https://www.strava.com/api/v3"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {access_token}"
        })

    def get_segment_by_id(self, segment_id: int) -> Dict[Any, Any]:
        """
        Get detailed information about a specific segment.
        
        Args:
            segment_id (int): The identifier of the segment
            
        Returns:
            dict: Segment details including name, distance, average grade, etc.
            
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        url = f"{self.base_url}/segments/{segment_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":

    with open(os.path.join("config","config.json"), "r", encoding="utf-8") as config:
        key = json.loads(config.read())['access']

    client = StravaClient(access_token=key)

    day = date.today().strftime("%Y-%m-%d")
    destination = f"/mnt/usbdrive/strava/downloads/segments/{day}"
    os.makedirs(destination, exist_ok=True)

    with open(os.path.join("config","segments.json"), "r", encoding="utf-8") as following:
        following = json.loads(following.read())

    segments = list(set(following))

    print(f"Segments to scrape: {len(segments)}")

    for count, s in enumerate(segments, start=1):

        try:
            cas = str(time.time()).split(".")[0]
            segment = client.get_segment_by_id(s)
            with open(os.path.join(destination, f"{s}_{cas}.json"), "w+", encoding="utf-8") as export:
                export.write(json.dumps(segment))
            print(f"{count}: {s} / {segment['name']}")
            if count % 100 == 0:
                time.sleep(960)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching segment: {e}")