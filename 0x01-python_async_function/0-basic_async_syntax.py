#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:13:00 2024

@Author: Caleb Kilonzi
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns
    the delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
