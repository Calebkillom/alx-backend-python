#!/usr/bin/env python3
""" The basics of async """"

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns
    the delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
