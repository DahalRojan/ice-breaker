import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        # Use mock data for testing
        linkedin_profile_url = "https://gist.githubusercontent.com/DahalRojan/2749b0440e0bfaa48e831339623574c8/raw/919c244bc1d1286bdf92612f12309b7e319bf1aa/rojandahal.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        # Use the actual API endpoint
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    
    # Check for successful request
    if response.status_code == 200:
        data = response.json()
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")
        return data
    else:
        # Handle errors (you can customize this part)
        print(f"Request failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    result = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/rojandahal/",
        mock=False
    )
    print(result)
