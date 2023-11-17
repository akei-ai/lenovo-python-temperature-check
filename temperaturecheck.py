import os
import psutil
import sys
import time
#check imple. later
SENSIBLE_TEMP_DEFAULT=80
SENSIBLE_DELAY_DEFAULT=2


try:
    t_target=int(sys.argv[1])
except ValueError:
    print("Invalid temperature input provided, setting sensible default:", SENSIBLE_TEMP_DEFAULT, "degrees celsius")
    t_target=SENSIBLE_TEMP_DEFAULT

try:
    sleep_target=int(sys.argv[2])
except ValueError:
    print("Invalid delay provided, setting sensible default:", SENSIBLE_DELAY_DEFAULT, "seconds")
    sleep_target=SENSIBLE_DELAY_DEFAULT


def main():
    while True:
        x1 = psutil.sensors_temperatures(fahrenheit=False)
  
        
        if x1["k10temp"][0][1] > t_target:
            os.system("ec4Linux enable")
            print("Enabling ExtremeCooling4Linux")
        else:
            os.system("ec4Linux disable")
            print("Disabling ExtremeCooling4Linux")
        print(x1["k10temp"][0][1])
        print(sleep_target)
        print(t_target)
        time.sleep(sleep_target)
        
        
    
    
if __name__ == "__main__":
    main()

