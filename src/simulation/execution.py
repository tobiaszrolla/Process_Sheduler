from src.models.process import Process


def execute_step(process: Process, current_time: int, quantum: int) -> int:
    """
        Executes a single CPU scheduling step for a given process.

        If the process has not started yet, initializes its execution state
        (start time and response time).

        The process is executed for a duration equal to the minimum of:
        - the given time quantum
        - the process remaining execution time

        After execution, the function updates process state and checks
        whether the process has finished.

        Args:
            process (Process): Process to execute
            current_time (int): Current simulation time
            quantum (int): Maximum allowed execution time slice

        Returns:
            int: Actual time the process was executed
    """

    if not process.is_started:
        process.start_time = current_time
        process.is_started = True
        process.response_time = current_time - process.arrival_time

    run_time = min(process.remaining_time, quantum)
    process.remaining_time -= run_time

    finish_time = current_time + run_time

    if process.remaining_time <= 0:
        process.is_finished = True
        process.completion_time = finish_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

    return run_time

