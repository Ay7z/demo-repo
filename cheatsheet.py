
##########numpy printing output cheatsheet##########

# Format specifications cheatsheet
# :<10    → left align, 10 spaces wide
# :>10    → right align, 10 spaces wide
# :>10,   → right align, 10 spaces, comma separator
# :>6.1f  → right align, 6 spaces, 1 decimal place
# :>6.2f  → right align, 6 spaces, 2 decimal places
# :.0f    → no decimal places
# :,      → just add comma separators

# ============================================
#       NUMPY UFUNCS - QUICK REFERENCE
# ============================================

import numpy as np

data = np.array([4, 9, 16, 25, 100])

# ── MATH FUNCTIONS ───────────────────────────

np.sqrt(data)        # Square root        → Risk calculations
np.abs(data)         # Remove negatives   → Variance analysis
np.round(data, 2)    # Round numbers      → Cleaning messy data
np.log(data)         # Logarithm          → Growth rate analysis

# ── STATISTICS ───────────────────────────────

np.sum(data)         # Total              → Revenue totals
np.mean(data)        # Average            → KPI benchmarking
np.max(data)         # Highest value      → Best performer
np.min(data)         # Lowest value       → Worst performer
np.median(data)      # Middle value       → Trend analysis
np.std(data)         # Spread of data     → Risk/consistency
np.var(data)         # Variance           → Volatility analysis
np.percentile(data, 75)  # Percentile     → Benchmarking

# ── USEFUL EXTRAS ────────────────────────────

np.cumsum(data)      # Running total      → Cumulative revenue
np.diff(data)        # Difference between elements → Month on month change
np.argmax(data)      # Index of highest   → Which month was best
np.argmin(data)      # Index of lowest    → Which month was worst
np.unique(data)      # Unique values only → Remove duplicates
np.sort(data)        # Sort ascending     → Ranking
np.where(data > 10, "High", "Low")  # IF logic → Categorizing

# ==================ufuncs=================

np.abs(array)       #→ remove negatives
np.round(array, n)   #round to n decimal places
np.sum(array)        #total
np.mean(array)       #average
np.max(array)        #highest
np.min(array)        #lowest
np.sqrt(array)       #square root