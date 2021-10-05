# ! @author: @ruhendd (Mudigonda Himansh)
# TODO 1: A CLI Application that manages todo lists
# TODO Commands: 
# ^ todo
# ^ todo add <<task>>
# ^ todo complete <<task_index>>
# ^ todo delete <<task_index>>

# imports here
import sys
from dataclasses import dataclass

@dataclass
class task:
    task_no: int
    task_name: str
    task_status: str = "open"


class main:      
    arguments_array = list()
    arguments_array = sys.argv
    arguments_array.pop(0)
    print(arguments_array)
    if arguments_array[0] == "add":
        if len(arguments_array) == 3:
            new_task = task(1, arguments_array[1], arguments_array[2])
            print(new_task)
        elif len(arguments_array) == 2:
            new_task = task(1, arguments_array[1])
            print(new_task)
        else:
            print(" :( This is an invalid input! Check and try again!")

main_runner = main()
main_runner 
