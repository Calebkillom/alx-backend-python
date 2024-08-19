#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:20:00 2024

@Author: Caleb Kilonzi
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    a list of all the delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    sorted_delays = []
    for delay in delays:
        i = 0
        while i < len(sorted_delays) and sorted_delays[i] < delay:
            i += 1
        sorted_delays.insert(i, delay)
    return sorted_delays
