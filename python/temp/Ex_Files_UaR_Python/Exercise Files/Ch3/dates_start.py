#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date

def main():
  today = date.today()
  print today.weekday()
  print today.month, today.year, today.day
  


if __name__ == "__main__":
  main();
  