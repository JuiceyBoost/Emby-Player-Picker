import sys
import subprocess
import os
import shutil
import tempfile

# Check if exactly two arguments are provided
if len(sys.argv) != 3:
    print("Error: Two arguments are required.")
    sys.exit(1)

# Retrieve the arguments
arg1 = sys.argv[1] # HLS Stream URL from Emby/Jellyfin
arg2 = sys.argv[2] # Resume time measured in Seconds

# Print the arguments for debugging purposes
print(f"Arguments received:\narg1: {arg1}\narg2: {arg2}")

# Path to the embedded executable within the PyInstaller package
exe_name = "emby_player_picker_main.exe"
temp_dir = tempfile.mkdtemp()
exe_path = os.path.join(temp_dir, exe_name)

try:
    # Extract the executable to a temporary directory
    with open(exe_path, 'wb') as exe_file:
        exe_file.write(open(os.path.join(sys._MEIPASS, exe_name), 'rb').read())

    # Launch the application in a new console window
    process = subprocess.Popen([exe_path, arg1, arg2], creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    # Wait for the process to complete
    process.wait()
finally:
    # Cleanup the temporary directory after the application has run
    shutil.rmtree(temp_dir)
