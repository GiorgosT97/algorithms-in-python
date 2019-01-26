import sys
import logging

import config

LOGGER = logging.getLogger(__name__)

PROCESSES = {
    'P1': 5,
    'P2': 3,
    'P3': 8,
    'P4': 6
}


def rr_arrival_is_zero(time_quantum):
    """ 
    Round Robin for Scheduling Processes with the assumption 
    that all processes arive at t = 0
    """
    processes_wating_time = dict()
    # Initiate Processes waiting time with 0
    for key in PROCESSES.keys():
        processes_wating_time[key] = 0

    # Start iterating the processes
    processes_finished = dict()
    while (True):
        for process in PROCESSES.keys():
            # If process has not finshed reduce its time
            if process not in processes_finished.keys():
                PROCESSES[process] -= time_quantum
                # If proc_time is < 0 add to finished
                if PROCESSES[process] <= 0:
                    processes_finished[process] = PROCESSES[process]
                for wating_proc in processes_wating_time.keys():
                    if wating_proc != process and wating_proc not in processes_finished.keys():
                        processes_wating_time[wating_proc] += time_quantum
            LOGGER.debug(f'PROCESSES: {PROCESSES}')
            LOGGER.debug(f'PROCESS WATING TIME: {processes_wating_time}')
            LOGGER.debug(f'PROCESS FINISHED: {processes_finished}\n')
        if processes_finished.keys() == PROCESSES.keys():
            for proc in processes_finished.keys():
                if processes_finished[proc] < 0:
                    LOGGER.debug(proc)
                    processes_wating_time[proc] += processes_finished[proc]
            LOGGER.debug(processes_wating_time)
            break
    average_waiting_time = 0
    for index, time in enumerate(processes_wating_time.values()):
        average_waiting_time += time
    average_waiting_time /= index + 1
    LOGGER.debug(f'Average waiting process time: {average_waiting_time}')
    return average_waiting_time

    def rr_time_quantum_fixed(time_quantum):
    """
    Round Robin for Scheduling Processes with the assumption 
    that all processes arive at t = 0 and time quantum can use
    more than one processes if one finish and there is time for 
    another one.
    """
    processes_wating_time = dict()
    # Initiate Processes waiting time with 0
    for key in PROCESSES.keys():
        processes_wating_time[key] = 0

    # Start iterating the processes
    processes_finished = dict()
    while (True):
        for process in PROCESSES.keys():
            # If process has not finshed reduce its time
            if process not in processes_finished.keys():
                PROCESSES[process] -= time_quantum
                # If proc_time is < 0 add to finished
                if PROCESSES[process] <= 0:
                    processes_finished[process] = PROCESSES[process]
                for wating_proc in processes_wating_time.keys():
                    if wating_proc != process and wating_proc not in processes_finished.keys():
                        processes_wating_time[wating_proc] += time_quantum
            LOGGER.debug(f'PROCESSES: {PROCESSES}')
            LOGGER.debug(f'PROCESS WATING TIME: {processes_wating_time}')
            LOGGER.debug(f'PROCESS FINISHED: {processes_finished}\n')
        if processes_finished.keys() == PROCESSES.keys():
            for proc in processes_finished.keys():
                if processes_finished[proc] < 0:
                    LOGGER.debug(proc)
                    processes_wating_time[proc] += processes_finished[proc]
            LOGGER.debug(processes_wating_time)
            break
    average_waiting_time = 0
    for index, time in enumerate(processes_wating_time.values()):
        average_waiting_time += time
    average_waiting_time /= index + 1
    LOGGER.debug(f'Average waiting process time: {average_waiting_time}')
    return average_waiting_time


if __name__ == '__main__':
    try:
        time_quantum = sys.argv[1]
        try:
            time_quantum = int(time_quantum)
        except ValueError:
            time_quantum = 1
            LOGGER.debug(f"Assuming time quantum is {time_quantum}")
    except IndexError:
        time_quantum = 1
        LOGGER.debug(f"Assuming time quantum is {time_quantum}")
    rr_arrival_is_zero(time_quantum)
