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
## 📉 Section 5.2: Essential Functionality (Part 1 - Reindexing)

This script maps out the low-level data and axis alignment mechanics in pandas, focusing on memory allocation during state changes.

### Key Architectural Concepts Covered:
* **Index Realignment:** How pandas maps existing data arrays onto newly requested label structures without altering original memory blocks.
* **Forward-Fill (`ffill`):** Temporal tracking and interpolation logic for handling gaps in sequential or time-series datasets.
* **2D Boundary Constraints:** Multi-axis alignment (handling dropped states vs introducing new structural nodes filled with `NaN`).
* **The `.loc` Exception Guardrail:** Verifying that while `.loc` offers high-speed index reordering, it enforces a strict runtime constraint (raising a `KeyError` if non-existent keys are requested), unlike `reindex()`.
*
## ✂️ Section 5.2: Essential Functionality (Part 2 - Dropping Entries)

This module handles dimensional reduction and safe data pruning across multiple axes inside pandas structures without mutating the baseline memory profile.

### Key Architectural Concepts Covered:
* **Immutability Safety:** Deep dive into how `drop()` creates filtered structural views/copies rather than executing immediate hard deletes in the parent memory address space.
* **Row Exclusions (`axis=0`):** Pruning custom indexing rows through sequential arrays without breaking surrounding index-label mappings.
* **Column Pruning (`axis=1` / `columns`):** High-speed vertical slicing. Compared modern keyword routing (`columns=["label"]`) with legacy NumPy-style dimension targeting (`axis="columns"`).
*
