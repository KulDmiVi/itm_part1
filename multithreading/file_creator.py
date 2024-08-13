import asyncio
import time

from aiofile import AIOFile


async def create_file(index):
    filename = f'file_{index}.txt'
    async with AIOFile(filename, 'w') as file:
        print(f'Запись в файл {index}')
        await file.write(str(index))
        await file.fsync()
    print(f'{filename} создан.')


async def create_files_concurrently():
    tasks = []
    for i in range(10):
        tasks.append(create_file(i))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(create_files_concurrently())
    print(f"Затраченное время: {time.time() - start_time} секунд.")