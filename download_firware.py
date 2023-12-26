import csv
import requests
import os
import time
from datetime import timedelta
from colorama import init, Fore, Style

# Initialize colorama
init()

def download_firmware(url, destination):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # Adjust the block size as needed
        start_time = time.time()
        downloaded = 0

        with open(destination, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                downloaded += len(data)
                elapsed_time = time.time() - start_time
                download_speed = downloaded / elapsed_time if elapsed_time > 0 else 0
                remaining_time = (total_size - downloaded) / download_speed if download_speed > 0 else 0
                print_progress(downloaded, total_size, elapsed_time, remaining_time, download_speed)

        print(f"\n{Fore.GREEN}Downloaded successfully: {destination}{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Error downloading firmware from {url}: {e}{Style.RESET_ALL}")

def print_progress(downloaded, total_size, elapsed_time, remaining_time, download_speed):
    progress = int(downloaded / total_size * 100)
    color = get_color(progress)
    print(
        f"\r{color}Progress: {progress}% | Downloaded: {format_size(downloaded)} | "
        f"Total: {format_size(total_size)} | Elapsed Time: {format_time(elapsed_time)} | "
        f"Remaining Time: {format_time(remaining_time)} | Download Speed: {format_size(download_speed)}/s{Style.RESET_ALL}",
        end="",
        flush=True,
    )

def get_color(progress):
    if progress < 10:
        return Fore.RED
    elif progress < 90:
        return Fore.YELLOW
    else:
        return Fore.GREEN

def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"

def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))

def is_firmware_downloaded(destination):
    return os.path.exists(destination)

def download_firmwares(csv_file, output_directory):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            link = row["download_link"].strip()
            filename = os.path.basename(link)
            destination = os.path.join(output_directory, filename)

            if not is_firmware_downloaded(destination):
                download_firmware(link, destination)
            else:
                print(
                    f"{Fore.CYAN}Firmware already downloaded: {filename}{Style.RESET_ALL}")

if __name__ == "__main__":
    csv_file = "D:/University/FYP/Scraper/firmware/tendaa.csv"  # Replace with the path to your CSV file
    output_directory = "downloaded_firmwares"  # Replace with the desired output directory

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_firmwares(csv_file, output_directory)
