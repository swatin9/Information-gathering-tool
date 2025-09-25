import socket

# Function to get IP address of a website
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Could not resolve the domain name"

print("✨ Information Gathering Tool ✨")
print("Type 'exit' to quit.\n")

# Loop for multiple websites
while True:
    website = input("Enter the website domain: ")
    if website.lower() == "exit":
        print("Exiting the tool... Bye! 👋")
        break
    ip_address = get_ip_address(website)
    print(f"IP Address of {website}: {ip_address}\n")
