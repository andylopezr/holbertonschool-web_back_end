#!/usr/bin/env python3
""" Module for storing the async_generator coroutine. """
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Waits for a second and yields a random number. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
