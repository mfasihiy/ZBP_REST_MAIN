import json
import re

def parse_http_response_from_file(response_file="response.json"):
    http_status = None
    json_response = None

    try:
        with open(response_file, "r") as file:
            lines = file.readlines()

        if not lines:
            print("❌ Error: Empty response file!")
            return None, None

        # Extract HTTP status code from the first line
        first_line = lines[0].strip()
        print("First line of response:", first_line)

        match = re.search(r"HTTP/1\.\d (\d+)", first_line)
        if match:
            http_status = int(match.group(1))
            print(f"Extracted HTTP Status: {http_status}")

            # Find where JSON starts (after an empty line)
            json_start_index = None
            for i, line in enumerate(lines):
                if line.strip() == "":  # JSON starts after the first empty line
                    json_start_index = i + 1
                    break

            if json_start_index is not None and json_start_index < len(lines):
                json_str = "".join(lines[json_start_index:]).strip()

                try:
                    json_response = json.loads(json_str)  # Parse JSON correctly
                    print("📜 Parsed JSON Response:", json.dumps(json_response, indent=4))
                except json.JSONDecodeError as e:
                    print(f"❌ JSON Parsing Error: {e}")
                    print("Raw JSON Data:", json_str)
                    json_response = None
            else:
                print("❌ Error: No JSON body found in response!")
        else:
            print("❌ Error: Could not find HTTP status in response file!")

    except FileNotFoundError:
        print("❌ Error: Response JSON file not found!")

    return http_status, json_response
