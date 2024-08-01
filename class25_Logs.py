import logging
import time
"""
Logs
"""

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -%(levelname)s -%(message)s",
                    handlers=[logging.StreamHandler()])

logging.debug("Esto es un mensaje DEBUG")
logging.info("Esto es un mensaje INFO")
logging.warning("Esto es un mensaje WARNING")
logging.error("Esto es un mensaje ERROR")
logging.critical ("Esto es un mensaje CRITICAL")

"""
Extra
"""

class TaskManager:
    
    def __init__(self)-> None:
        self.tasks = {}
        
    def add_task(self, name: str, description:str):
        start_time =time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida:{name}.")
        else:
            logging.warning(f"se ha intentado añadir una tarea que ya existe:{name}.")
        logging.debug(f"Número de tareas:{len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)        
        
            
    def delete_task(self,name:str):
        start_time =time.time() 
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"se ha eliminado la tarea:{name}.")
        else:
            logging.error(f"Se ha intentado eliminar una tarea que no existe:{name}.")   
        logging.debug(f"Número de tareas:{len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)
                
    def list_task(self):
        start_time =time.time()
        if self.tasks:
            logging.info(f"Se va a imprimir la lista de tareas.")
            for name, description in self.tasks.items():
                print(f"{name}-{description}")
        else:
            logging.info(f"No hay tareas para mostrar.")
        end_time = time.time()        
        self._print_time(start_time, end_time)
    
    def _print_time(start_time, end_time):
        logging.debug(
            f"Tiempo de la ejecución:{end_time - start_time:6f} segundos")
                

tasks_manager = TaskManager()
tasks_manager.list_task()                
tasks_manager.add_task("Pan","Comprar 5 barras de pan")                
tasks_manager.add_task("Python","Estudiar Python")                
tasks_manager.list_task()                
tasks_manager.delete_task("Python")                
tasks_manager.list_task()                
tasks_manager.add_task("Pan","Comprar 5 barras de pan")                
tasks_manager.delete_task("Python")                