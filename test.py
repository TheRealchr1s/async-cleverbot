"""
MIT License

Copyright (c) 2018-2021 chr1s

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
import aiohttp
import async_cleverbot as ac
import os

CB_TOKEN = os.environ.get("CB_TOKEN")
if not CB_TOKEN:
    raise OSError("Token isn't an env var.")

cb = ac.Cleverbot(CB_TOKEN, context=ac.DictContext())


async def main():
    print((await cb.ask("hello!", 1)).text)
    print(cb.context._storage)

    # await asyncio.sleep(1)

    # await cb.ask("how are you?", 1)
    # print(cb.context._storage)


asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(cb.close())