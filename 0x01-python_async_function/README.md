# Python Async Function Project

This project explores asynchronous programming in Python, focusing on coroutines, tasks, and measuring execution time. It consists of five tasks that build upon each other to demonstrate various aspects of async programming.

## Project Structure

- `0-basic_async_syntax.py`: Implements a basic asynchronous coroutine.
- `1-concurrent_coroutines.py`: Demonstrates running multiple coroutines concurrently.
- `2-measure_runtime.py`: Measures the runtime of asynchronous operations.
- `3-tasks.py`: Introduces the concept of asyncio Tasks.
- `4-tasks.py`: Modifies previous implementations to work with Tasks.

## Tasks Overview

### 0. The basics of async

Implements an asynchronous coroutine `wait_random(max_delay: int = 10) -> float` that waits for a random delay between 0 and `max_delay` seconds and returns it.

### 1. Let's execute multiple coroutines at the same time with async

Implements an async routine `wait_n(n: int, max_delay: int) -> List[float]` that spawns `wait_random` n times with the specified `max_delay`. Returns a list of all the delays in ascending order.

### 2. Measure the runtime

Implements a `measure_time(n: int, max_delay: int) -> float` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

### 3. Tasks

Implements a function `task_wait_random(max_delay: int) -> asyncio.Task` that returns an `asyncio.Task` for the `wait_random` coroutine.

### 4. Tasks

Implements a function `task_wait_n(n: int, max_delay: int) -> List[float]` that is nearly identical to `wait_n` but uses `task_wait_random`.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- pycodestyle 2.5.x

## Usage

Each file can be run independently. For example:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

## Style and Documentation

- All files use the `#!/usr/bin/env python3` shebang.
- Code follows pycodestyle style (version 2.5.x).
- All modules and functions have docstrings.
- All functions are type-annotated.
