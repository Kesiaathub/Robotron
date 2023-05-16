import time

while True:
    # Clear the console (optional)
    print('\033c', end='')
    
    # Get the current time
    current_time = time.strftime("%H:%M:%S", time.localtime())
    
    # Print the current time
    print("Current Time:", current_time)
    
    # Wait for 1 second
    time.sleep(1)
