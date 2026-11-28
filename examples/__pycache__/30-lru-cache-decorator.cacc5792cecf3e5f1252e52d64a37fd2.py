import functools
import functools

# apl-source:1
# مثال 30 — كاش LRU مع functools
# apl-source:2
# LRU Cache with Decorators
# apl-source:3
# Demonstrates: functools cache decorator, memoization
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/30-lru-cache-decorator.apl
# apl-source:6

# apl-source:7
@functools.lru_cache(128)
# apl-source:8
def دالة_فيب(ن):
    # apl-source:9
    if ن < 2:
        # apl-source:10
        return ن
    # apl-source:11
    return فيب(ن - 1) + فيب(ن - 2)
# apl-source:12

# apl-source:13
فيب = دالة_فيب
def دالة_فيب_بطيء(ن):
    # apl-source:14
    if ن < 2:
        # apl-source:15
        return ن
    # apl-source:16
    return فيب_بطيء(ن - 1) + فيب_بطيء(ن - 2)
# apl-source:17

# apl-source:18
فيب_بطيء = دالة_فيب_بطيء
print("=== كاش LRU ===")
# apl-source:19
print("")
# apl-source:20
print("فيب(20) مع الكاش : " + str(فيب(20)))
# apl-source:21
print("فيب(30) مع الكاش : " + str(فيب(30)))
# apl-source:22
print("فيب(50) مع الكاش : " + str(فيب(50)))
# apl-source:23
print("")
# apl-source:24
print("بدون كاش فيب(20) : " + str(فيب_بطيء(20)))
# apl-source:25
print("")
# apl-source:26
print("الكاش يجعل الاستدعاء الثاني فورياً لأن النتيجة محفوظة.")
# apl-source:27
