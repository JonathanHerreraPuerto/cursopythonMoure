import datetime
import time
import asyncio
"""
Asincronía
"""

async def task(name:str, duration:int):
    print(
        f"Tarea:{name}. Duración: {duration}s . Inicio: {datetime.datetime.now()}"
        )
    await asyncio.sleep(duration)
    
    print(
    f"Tarea:{name}. Fin: {datetime.datetime.now()}"
    )

asyncio.run(task("1", 2))


"""
Extra
"""  

async def async_tasks():
    await asyncio.gather(task("C",10),task("B",7),task("A",3))  
    await task("D", 1)

asyncio.run(async_tasks())