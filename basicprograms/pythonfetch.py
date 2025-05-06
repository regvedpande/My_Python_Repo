import asyncio

async def fetch_data_from_api_1():
    print("Fetching data from API 1...")
    await asyncio.sleep(2)  # Simulate I/O delay
    print("Data received from API 1")
    return {"api": 1, "data": "foo"}

async def fetch_data_from_api_2():
    print("Fetching data from API 2...")
    await asyncio.sleep(3)  # Simulate I/O delay
    print("Data received from API 2")
    return {"api": 2, "data": "bar"}

async def main():
    # Run both API calls concurrently
    task1 = asyncio.create_task(fetch_data_from_api_1())
    task2 = asyncio.create_task(fetch_data_from_api_2())

    print("Waiting for both APIs to respond...")
    results = await asyncio.gather(task1, task2)
    print("Both responses received:", results)

# Python 3.7+
if __name__ == "__main__":
    asyncio.run(main())