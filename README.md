# Pywhereisrunning
[![Build Status](https://travis-ci.org/atomse/pywhereisrunning.svg?branch=master)](https://travis-ci.org/atomse/pywhereisrunning)

To see where the python script is running when the script is running.

Basically, it uses SIGUSR1 to send the signal to the python script, the script get the signal and 
use the frame to display where the script is running.



## Installation


```bash
pip install pywhereisrunning
```



## Usage


Just

```python
import pywhereisrunning
```
to make the function available.


when you're run the script, use 

* `pywhereisrunning $(filename)`

to show where the script is running.

After the command, will show
```bash
  File "src/preprocess.py", line 50, in <module>
    click_df,train_user,test_user=merge_files()
  File "src/preprocess.py", line 36, in merge_files
    click_df=click_df.fillna(-1)
  File "/home/sky/.conda/envs/py3.6/lib/python3.6/site-packages/pandas/core/frame.py", line 4153, in fillna
    downcast=downcast,
  File "/home/sky/.conda/envs/py3.6/lib/python3.6/site-packages/pandas/core/generic.py", line 6237, in fillna
    value=value, limit=limit, inplace=inplace, downcast=downcast
```




## TODOS


[x] `pywhereisrunning + $(filename)`
