import asyncio
import aiohttp
import time


async def get_url(session, url, semaphore):
    async with semaphore:
        response = await session.get(url)
        return response.status


async def limited_requests(url, limit,  task_count):
    sem = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_url(session, url, sem)) for _ in range(task_count)]
        return await asyncio.gather(*tasks)

def status_writer(statuses):
    with open("statuses.txt", "w") as file:
        for status in statuses:
            file.write(f"{status}\n")

async def main():
    url = "http://example.com"
    limit = 10
    task_count = 50
    start_time = time.time()
    statuses = await limited_requests(url, limit, task_count)
    status_writer(statuses)
    print(f"Затраченное время: {time.time() - start_time} секунд.")


if __name__ == "__main__":
    asyncio.run(main())
