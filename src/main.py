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
    priority: int = 1  # 0 1 2 || Lower number higher priority


class main:
    def _check_priority(priority):
        if priority >= 0:
            if priority < 3:
                return 1
        return 0

    arguments_array = list()
    arguments_array = sys.argv
    arguments_array.pop(0)
    #print(arguments_array)
    if arguments_array[0] == "add":
        if len(arguments_array) == 4:
            priority_flag = _check_priority(int(arguments_array[3]))
            print(priority_flag)
            if priority_flag:
                new_task = task(1, arguments_array[1], arguments_array[2],
                                arguments_array[3])
                print(new_task)
            else:
                print("Priority Values only lie between 0 and 2 (inclusive)")
        elif len(arguments_array) == 3:
            if arguments_array[2].isdigit():
                new_task = task(1,
                                arguments_array[1],
                                priority=arguments_array[2])
            else:
                new_task = task(1, arguments_array[1], arguments_array[2])
            print(new_task)
        elif len(arguments_array) == 2:
            new_task = task(1, arguments_array[1])
            print(new_task)
        else:
            print(" :( This is an invalid input! Check and try again!")


main_runner = main()
main_runner
