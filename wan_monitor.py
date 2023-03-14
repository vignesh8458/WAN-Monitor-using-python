
import pywifi
import time
import speedtest
import smtplib
import datetime
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up email credentials
from_address = "vignesh8458@gmail.com"
to_address = "vignesh8458@gmail.com"
password = "enter your app password"
smtp_server = "smtp.gmail.com"

# Set up Wi-Fi interfaces
wifi = pywifi.PyWiFi()
ifaces = wifi.interfaces()

# Define Wi-Fi profiles
profiles = [
    {
        'ssid': 'prakash',
        'password': 'malignant'
    }
]

# Connect to Wi-Fi networks
for i, iface in enumerate(ifaces):
    profile = pywifi.Profile()
    profile.ssid = profiles[i]['ssid']
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = profiles[i]['password']
    iface.remove_all_network_profiles()
    iface.connect(iface.add_network_profile(profile))

# Wait for Wi-Fi connection
while any(iface.status() != pywifi.const.IFACE_CONNECTED for iface in ifaces):
    time.sleep(1)

# Run speed test and generate report for each interface
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Wi-Fi Speed Test Report"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
body = f"Report generated at {now}\n\n"
for i, iface in enumerate(ifaces):
    ssid = profiles[i]['ssid']
    print(f"Testing download speed for {ssid}...")
    
    # Get public IP address and ISP provider
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ip_address = ip_request.json()['ip']
    isp_request = requests.get('https://get.geojs.io/v1/ip/geo.json')
    isp_provider = isp_request.json()['organization_name']
    
    # Run speed test
    st = speedtest.Speedtest()
    download_speed = st.download()
    print(f"Download speed: {download_speed / 1e6} Mbps")
    upload_speed = st.upload()
    print(f"Upload speed: {upload_speed / 1e6} Mbps")
    ping_latency = st.results.ping
    print(f"Latency: {ping_latency} ms")

        # Add results to email body
    body += f"Wi-Fi {iface.name()} connected to {ssid}:\n"
    body += f"Download speed: {download_speed / 1e6} Mbps\n"
    body += f"Upload speed: {upload_speed / 1e6} Mbps\n"
    body += f"Latency: {ping_latency} ms\n"
    body += f"Public IP address: {ip_address}\n"
    body += f"ISP provider: {isp_provider}\n\n"
    msg.attach(MIMEText(body, 'plain'))

    # Send email message
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.login(from_address, password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()


print("Report sent by email")


# Disconnect from Wi-Fi
iface.disconnect()

# Define Wi-Fi profiles
profiles = [
    {
        'ssid': 'realme',
        'password': '12345678'
    }
]

# Connect to Wi-Fi networks
for i, iface in enumerate(ifaces):
    profile = pywifi.Profile()
    profile.ssid = profiles[i]['ssid']
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = profiles[i]['password']
    iface.remove_all_network_profiles()
    iface.connect(iface.add_network_profile(profile))

# Wait for Wi-Fi connection
while any(iface.status() != pywifi.const.IFACE_CONNECTED for iface in ifaces):
    time.sleep(1)

# Run speed test and generate report for each interface
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Wi-Fi Speed Test Report"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
body = f"Report generated at {now}\n\n"
for i, iface in enumerate(ifaces):
    ssid = profiles[i]['ssid']
    print(f"Testing download speed for {ssid}...")
    
    # Get public IP address and ISP provider
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ip_address = ip_request.json()['ip']
    isp_request = requests.get('https://get.geojs.io/v1/ip/geo.json')
    isp_provider = isp_request.json()['organization_name']
    
    # Run speed test
    st = speedtest.Speedtest()
    download_speed = st.download()
    print(f"Download speed: {download_speed / 1e6} Mbps")
    upload_speed = st.upload()
    print(f"Upload speed: {upload_speed / 1e6} Mbps")
    ping_latency = st.results.ping
    print(f"Latency: {ping_latency} ms")


    


    # Add results to email body
    body += f"Wi-Fi {iface.name()} connected to {ssid}:\n"
    body += f"Download speed: {download_speed / 1e6} Mbps\n"
    body += f"Upload speed: {upload_speed / 1e6} Mbps\n"
    body += f"Latency: {ping_latency} ms\n"
    body += f"Public IP address: {ip_address}\n"
    body += f"ISP provider: {isp_provider}\n\n"
msg.attach(MIMEText(body, 'plain'))

# Send email message
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.login(from_address, password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()


print("Report sent by email")
