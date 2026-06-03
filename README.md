# Process Scheduler

This is a project created for a university class. It implements four CPU scheduling algorithms:
FCFS, LCFS, SJF, and Round-Robin.

It also provides a research environment and a graphical user interface (GUI).  
The project is written in Python.

---

## Research Environment

You can create process groups with custom I/O waiting times and CPU burst ranges.  
It is also possible to specify:

- number of I/O operations per process
- maximum arrival time
- mixing multiple process groups

For the execution engine, you can configure:
- scheduling algorithm
- simulation start time
- simulation end time

---

## How to Run

1. Clone the repository

2. Create a virtual environment:
    ```bash
    python -m venv path/to/venv
    ```

3. Activate the virtual environment:

    Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

    Windows:
    ```bash
    venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run app:
    ```bash
    python main.py
    ```
    
