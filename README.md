# pandas-core-foundation
Text book analysis and practical mechanics of pandas from Wes Mckinney's book
# Pandas Core Foundations

This repository contains my step-by-step implementation, mechanics, and deep dives into the **pandas** library, inspired by Wes McKinney's *"Python for Data Analysis"*.

## What I Learned Today (Section 5.1: Series)
- **Data Labels:** How a `Series` wraps a NumPy array and maps it to a `RangeIndex` or custom labels.
- **Index Preservation:** Operations like boolean filtering and mathematical functions (`np.exp`) preserve the index-value link.
- **Data Alignment:** Automatic outer-join alignment during arithmetic operations, where mismatched labels generate `NaN` values.
- **Metadata:** Managing `name` attributes for both the Series object and its internal index.
-# 📊 Pandas Core Foundations - Section 5.1

This module contains the complete bottom-up engineering implementation of pandas data structures and underlying index mechanics, based on deep-dive textbook analysis.

## ⚡ Core Architecture Implemented:
1. **DataFrame Operations:** Heterogeneous column types, scalar broadcasting, array assignments, and shape constraints.
2. **Memory Mechanics:** `loc` (label-based) vs `iloc` (position-based) extraction, View vs Copy data slicing safety.
3. **Index Deep-Dive:** Micro-analysis of Index Object immutability, duplicate label handling, and Set Logic operations (`union`, `intersection`, `difference`).

*Built consistently as part of the Strategic AI Hardware & Machine Learning development plan.*
