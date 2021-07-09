import asyncio

# native coroutine
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


# native coroutin
async def main():
    # Execute three async count() concurrently.
    # return a list of values if any.
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time

    s = time.perf_counter()

    # entry point for async program.
    # Create an event loop and exit by closing it.
    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
