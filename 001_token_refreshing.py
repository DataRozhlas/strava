import json
import os
import subprocess

def refresh_strava_token():

    with open(os.path.join("config","config.json"), "r", encoding="utf-8") as config_in:
        config = json.loads(config_in.read())

    # Construct the curl command
    curl_command = [
        'curl',
        '-X', 'POST',
        'https://www.strava.com/api/v3/oauth/token',
        '-d', f'client_id={config["id"]}',
        '-d', f'client_secret={config["secret"]}',
        '-d', 'grant_type=refresh_token',
        '-d', f'refresh_token={config["refresh"]}'
    ]

    try:
        # Execute the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)
        if result.stderr:
            print("Errors:", result.stderr)

        response_data = json.loads(result.stdout)

        config['refresh'] = response_data['refresh_token']
        config['access'] = response_data['access_token']

        with open(os.path.join("config","config.json"), "w+", encoding="utf-8") as config_out:
            config_out.write(json.dumps(config))

    except subprocess.SubprocessError as e:
        print(f"Error executing curl command: {e}")

if __name__ == "__main__":
    refresh_strava_token()