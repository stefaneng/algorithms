# Activity-Selection Problem

Schedule activities that share a resource.

## Problem Description
    - Let S = {a_1,a_2,...,a_n} be a set of activities.
    - When an activities is active, then none of the others can be.
    - Each activity a_i has a start time s_i and finish time f_i.
    - Activities are compatible if intervals [s_i, f_i) and [s_j, f_j) do not overlap.
    - Goal: Select a maximum-size subset of mutually compatible activities.
