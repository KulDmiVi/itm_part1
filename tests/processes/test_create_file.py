import os
import pytest
from aiofile import AIOFile
from multithreading.file_creator import create_files_concurrently
pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_create_files_concurrently(monkeypatch):
    await create_files_concurrently()
    for i in range(10):
        filename = f'file_{i}.txt'
        if os.path.exists(filename):
            os.remove(filename)

    await create_files_concurrently()

    for i in range(10):
        filename = f'file_{i}.txt'
        assert os.path.exists(filename)
        async with AIOFile(filename, 'r') as file:
            content = await file.read()
            assert content == str(i)

    for i in range(10):
        os.remove(f'file_{i}.txt')


if __name__ == "__main__":
    pytest.main()
