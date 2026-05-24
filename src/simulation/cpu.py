from src.models.process import Process, ProcessState

def execute_cpu_step(process: Process, current_time: float, quantum: float) -> float:

    if process.is_finished():
        return 0

    if process.start_time is None:
        process.start_time = current_time
        process.response_time = current_time - process.arrival_time

    process.state = ProcessState.RUNNING

    run_time = min(process.cpu_bursts[0], quantum)
    process.cpu_bursts[0] -= run_time

    if process.cpu_bursts[0] > 0:
        process.state = ProcessState.READY
    else:
        process.cpu_bursts.popleft()

        if process.io_bursts:
            process.state = ProcessState.WAITING
        elif not process.cpu_bursts:
            process.state = ProcessState.FINISHED
            process.completion_time = current_time + run_time
            process.turnaround_time = process.completion_time - process.arrival_time

    return run_time