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

    def get_my_activities(self):
        """
        Get detailed information about a specific segment.
        
        Args:
            segment_id (int): The identifier of the segment
            
        Returns:
            dict: Segment details including name, distance, average grade, etc.
            
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        url = f"{self.base_url}/athlete/activities"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":

    with open(os.path.join("config","config.json"), "r", encoding="utf-8") as config:
        key = json.loads(config.read())['access']

    client = StravaClient(access_token=key)

    day = date.today().strftime("%Y-%m-%d")
    destination = f"downloads/my_activities/"
    os.makedirs(destination, exist_ok=True)

    
    activities = client.get_my_activities()
    with open(os.path.join(destination, f"my_activities.json"), "w+", encoding="utf-8") as export:
        export.write(json.dumps(activities))