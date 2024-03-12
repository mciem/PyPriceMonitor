from datetime  import datetime
from threading import RLock

import os

class Console:
    @staticmethod
    def clear():
        os.system("cls")

    @staticmethod
    def log(log_type: str, text: str = "", var: dict = {}, time: float = 0.0):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
            
        if log_type == "INP":
            print(f"\033[97m{current_time} \033[90m{log_type} \033[97m{text} » ", end="")
            return input()
            
        elif var != {}:
            text += f"\033[90m |"
                
            i = 0
            for v,k in var.items():
                text += f" \033[97m{v} » \033[90m{k}"
                if i != len(var)-1:
                    text += f"\033[97m,"
                        
                i += 1
                
        if time == 0.0:
            print(f"\033[97m{current_time} \033[90m{log_type} \033[97m{text}\033[97m")
        else:
            print(f"\033[97m{current_time} \033[90m{log_type} \033[97m{text} \033[90m(\033[97m{time:.2f}s\033[90m)\033[97m")