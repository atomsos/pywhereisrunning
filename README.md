# Pywhereisrunning


To see where the python script is running when the script is running.

Basically, it uses SIGUSR1 to send the signal to the python script, the script get the signal and 
use the frame to display where the script is running.




## Usage


Just

```python
import pywhereisrunning
```
to make the function available.


when you're run the script, use 

* `kill -SIGUSR1 $(PID)`
* `pywhereisrunning $(filename)`

to show where the script is running.

After the command, will show
`main.py func=main line=9:`
