# =================================================================
# WEEK 9: FILE MANIPULATION AND DATA PERSISTENCE
# =================================================================
import os

# // Exercise 1: Writing and Creating a File
# // Create a simulated configuration file for a sensor system.
def create_config():
    config_data = [
        "Sensor_ID: ESP32_Node_01\n",
        "Sampling_Rate: 1000Hz\n",
        "VCC_Target: 3.3V\n",
        "Mode: High_Precision"
    ]
    try:
        with open("system_config.txt", "w") as f:
            f.writelines(config_data)
        print("[SUCCESS] Configuration file created.")
    except Exception as e:
        print(f"[ERROR] Could not write file: {e}")

# // Exercise 2: Reading Files in Different Ways
# // Demonstrate reading the entire content and reading line-by-line.
def read_config():
    if not os.path.exists("system_config.txt"):
        print("[ERROR] File not found.")
        return

    print("\n--- Reading Entire File ---")
    with open("system_config.txt", "r") as f:
        print(f.read())

    print("--- Reading Line by Line (Processed) ---")
    with open("system_config.txt", "r") as f:
        for line in f:
            # // Strip() removes trailing newlines '\n'
            print(f"Setting found: {line.strip()}")

# // Exercise 3: Appending Data (Logging)
# // Simulate a data logger that appends new timestamped readings.
def log_sensor_reading(value):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Current Reading: {value}A\n"
    
    with open("sensor_log.txt", "a") as f:
        f.write(log_entry)
    print(f"[LOG] Saved reading: {value}A")

# // Exercise 4: Handling Errors (Try-Except)
# // Attempt to read a non-existent file and handle the FileNotFoundError.
def safe_read(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Warning: The file '{filename}' does not exist."

# // Exercise 5: Working with Binary Files (Conceptual)
# // Demonstrate how to copy an image file (binary mode).
def backup_image(source_img, target_img):
    try:
        with open(source_img, "rb") as f_src:
            data = f_src.read()
            with open(target_img, "wb") as f_dest:
                f_dest.write(data)
        print(f"[SUCCESS] Image backed up to {target_img}")
    except FileNotFoundError:
        print("[SKIP] No image found to backup.")

# -----------------------------------------------------------------
# EXECUTION AND TESTING
# -----------------------------------------------------------------

# // 1. Setup the initial system
create_config()

# // 2. Read and parse the setup
read_config()

# // 3. Simulate continuous logging
print("\n--- Starting Data Logger ---")
log_sensor_reading(0.452)
log_sensor_reading(0.458)
log_sensor_reading(0.449)

# // 4. Test error handling
print("\n--- Error Handling Test ---")
print(safe_read("non_existent_data.csv"))

# // 5. Check file information using 'os' module
file_size = os.path.getsize("system_config.txt")
print(f"\n[INFO] 'system_config.txt' size: {file_size} bytes.")

# =================================================================
# END OF WEEK 9 PRACTICE
# =================================================================