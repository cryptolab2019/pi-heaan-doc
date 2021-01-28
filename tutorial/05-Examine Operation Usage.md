# Examine Operation Usage

The Operation Usage report provides convenient method for developing HE algorithm. The report enables to check estimated operation time of the algorithm which is the clue to improve the performance of the algorithm. Operation Usage provides the estimated time of the algorithm for each operation so we can build our algorithm more efficiently.

```python
>>> print(context)
=========== Operation Usage (in single thread) ===========
==========================================================
OP_TYPE         TIME_UNIT       NUM_USAGE       TIME_USAGE
----------------------------------------------------------
encrypt         0.191           1               0.191
decrypt         0.032           1               0.032
----------------------------------------------------------
                *** Total estimated time unit : 0.223
```