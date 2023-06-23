import speedtest

def measure_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert to megabits per second
    upload_speed = st.upload() / 1000000  # Convert to megabits per second

    return download_speed, upload_speed

# Example usage
download_speed, upload_speed = measure_internet_speed()
print("Download Speed:", round(download_speed, 2), "Mbps")
print("Upload Speed:", round(upload_speed, 2), "Mbps")
