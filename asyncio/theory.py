from random import randint
import time
import asyncio

def odds(start, stop):
    for odd in range(start, stop+1, 2):
        yield odd

async def randn():
    await asyncio.sleep(3)
    return randint(1, 10)

async def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)
    
    start = time.perf_counter()
    randomNum = await randn()
    elapsed = time .perf_counter() - start
    print(f'{randomNum} took {elapsed:0.3f} seconds.')

    start = time.perf_counter()
    randomNum = await asyncio.gather(*(randn() for _ in range(10)))
    elapsed = time .perf_counter() - start
    print(f'{randomNum} took {elapsed:0.3f} seconds.')


if __name__ == "__main__":
    asyncio.run(main())