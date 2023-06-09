from rich.table import Table
from rich import print
 
table = Table(title="First table using rich!")
table.add_column("Language", justify="center", style="bright_yellow", no_wrap=True)
table.add_column("Year Initially Released", style="green")
table.add_column("Most recent version", justify="right", style="red")
 
table.add_row( "Python", "1991", "3.9.1")
table.add_row( "R", "1993", "4.0.3")
table.add_row( "Java", "1995", "Java 15")
 
print(table)




from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

print(table)


