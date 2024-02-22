import requests

# Cloudflare API URL
base_url = "https://api.cloudflare.com/client/v4"

# Replace these with your actual details
api_token = "YOUR_CLOUDFLARE_API_TOKEN"
zone_id = "YOUR_ZONE_ID"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}

def list_dns_records(zone_id):
    """List all DNS records for a given zone."""
    list_url = f"{base_url}/zones/{zone_id}/dns_records"
    response = requests.get(list_url, headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        print("Failed to retrieve DNS records.")
        return None

def delete_dns_record(zone_id, record_id):
    """Delete a DNS record by ID."""
    delete_url = f"{base_url}/zones/{zone_id}/dns_records/{record_id}"
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 200:
        print(f"Deleted DNS record {record_id}")
    else:
        print(f"Failed to delete DNS record {record_id}")

def delete_all_dns_records(zone_id):
    """Delete all DNS records for a zone after confirmation."""
    dns_records = list_dns_records(zone_id)
    if dns_records:
        print("DNS Records to be deleted:")
        for record in dns_records:
            print(f"ID: {record['id']}, Type: {record['type']}, Name: {record['name']}, Content: {record['content']}")
        
        # Ask for confirmation
        confirmation = input("Do you really want to delete all listed DNS records? (yes/no): ")
        if confirmation.lower() == "yes":
            for record in dns_records:
                delete_dns_record(zone_id, record['id'])
        else:
            print("Operation cancelled.")

if __name__ == "__main__":
    delete_all_dns_records(zone_id)
