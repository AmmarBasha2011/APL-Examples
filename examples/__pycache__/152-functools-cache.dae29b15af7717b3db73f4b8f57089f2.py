import functools
import functools

# apl-source:1
# مثال 152 — التخزين المؤقت للدوال
# apl-source:2
# Function caching with lru_cache
# apl-source:3
# Demonstrates: @كاش_مؤقت_دالة، recursion
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/152-functools-cache.apl
# apl-source:6

# apl-source:7
@functools.lru_cache
# apl-source:8
def فيب(ن):
    # apl-source:9
    if ن < 2:
        # apl-source:10
        return ن
    # apl-source:11
    return فيب(ن - 1) + فيب(ن - 2)
# apl-source:12

# apl-source:13
print("فيب(10) =", فيب(10))
# apl-source:14
print("فيب(50) =", فيب(50))
# apl-source:15
print("فيب(90) =", فيب(90))
# apl-source:16
print("معلومات الكاش:", فيب.cache_info().hits > 0)
# apl-source:17
