from src.models.process import Process, ProcessState


from src.models.process import Process, ProcessState


def execute_io_step(process: Process, delta_time: float):
    if process.state != ProcessState.WAITING:
        return

    process.io_bursts[0] -= delta_time

    if process.io_bursts[0] > 0:
        return

    if process.io_bursts:
        process.io_bursts.popleft()

    if process.cpu_bursts:
        process.state = ProcessState.READY
    else:
        process.state = ProcessState.FINISHED