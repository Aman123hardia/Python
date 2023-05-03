# import time
# from rich.progress import track

# def loop_last(values=[1,2,3,4,5,6,6]):
                
#    iter_values = iter(values)                                  
#    try:                                                        
#        previous_value = next(iter_values)                      
#    except StopIteration:                                       
#        return                                                  
#    for value in iter_values:                                   
#        yield False, previous_value                             
#        previous_value = value                                  
#        yield True, previous_value 
       

# d=loop_last()

# for i in  track(d,description="Processing..."):
#     time.sleep(2) 


# import time

# from rich.progress import Progress 
# a=Progress()
# task1 = a.add_task("[red]Downloading...", total=1000)
# task2 = a.add_task("[green]Processing...", total=1000)
# task3 = a.add_task("[cyan]Cooking...", total=1000)
# while not a.finished:
#     a.update(task1, advance=0.5)
#     a.update(task2, advance=0.3)
#     a.update(task3, advance=0.9)
#     time.sleep(0.02)

from rich.progress import track
import time
for num in track(range(100)):
    time.sleep(1)
    print(num * 2)