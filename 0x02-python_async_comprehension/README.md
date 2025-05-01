# Python Async Comprehension

This project explores asynchronous comprehensions and generators in Python 3.7. It includes three tasks that demonstrate how to implement asynchronous generators, use async comprehensions, and measure runtime of parallel asynchronous operations.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle 2.5.x

## Files

1. **0-async_generator.py**: Contains a coroutine called `async_generator` that yields 10 random numbers.
2. **1-async_comprehension.py**: Contains a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension.
3. **2-measure_runtime.py**: Contains a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel and measures the total runtime.

## Tasks Explanation

### 0. Async Generator
This task demonstrates how to create an asynchronous generator that yields random values. The generator loops 10 times, each time awaiting 1 second and then yielding a random float between 0 and 10.

### 1. Async Comprehensions
This task demonstrates how to use async comprehensions to collect values from an async generator. The function `async_comprehension()` uses an async comprehension to collect 10 random numbers from `async_generator()`.

### 2. Run time for four parallel comprehensions
This task demonstrates how to run multiple asynchronous comprehensions in parallel and measure the total runtime. The function `measure_runtime()` runs `async_comprehension()` four times in parallel using `asyncio.gather()` and measures the total runtime.

The total runtime is roughly 10 seconds because each call to `async_comprehension()` collects 10 values from `async_generator()`, with each value taking 1 second to generate. Since the four calls to `async_comprehension()` are run in parallel, the total runtime is only about 10 seconds (the time it takes for one call to complete) rather than 40 seconds (if they were run sequentially).
