# Data Comparator
Compares data from ```.csv``` file (filePath column) and content of ```./files``` directory

## How to launch
1. Create ```singleDisciplineDirectory``` directory in project root folder
2. Add ```files``` and ```data.csv``` to ```singleDisciplineDirectory```
3. Run ```python main.py -sd```

## What will happen
- The program will create new data.csv with all old entries that have related
  file in ```files``` directory
- It will also delete extra files that are not mentioned in ```data.csv```
