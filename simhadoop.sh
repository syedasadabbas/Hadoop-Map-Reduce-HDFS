# #!/usr/bin/env bash

# cat r100.txt | ./mapper.py > mapout.txt
# sort mapout.txt | ./combiner.py > comout.txt 
# sort comout.txt | ./reducer.py > results.txt

#!/bin/bash

# Run mapper.py
echo "Running mapper.py..."
python mapper.py < r100.txt > mapout.txt

# Run combiner.py
echo "Running combiner.py..."
python combiner.py < mapout.txt > comout.txt

# Run reducer.py
echo "Running reducer.py..."
python reducer.py < comout.txt > results.txt

echo "Process complete."
