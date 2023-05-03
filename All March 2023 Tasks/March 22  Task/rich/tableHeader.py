from rich import print
from rich.table import Column,Table
table = Table(
    "Released",
    "Title",
    Column(header="Box Office", justify="right" ,style="red" ),
    title="Star Wars Movies"
)

