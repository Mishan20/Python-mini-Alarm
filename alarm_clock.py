from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\003[H"

def alarm(second):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < second:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = second - time_elapsed
        minutes_left = time_left // 60
        second_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d}:{second_left:02d}")
        
    playsound("Alarm.mp3")
    
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)