
# apl-source:1
# مثال 33 — القوائم فهم comprehensions
# apl-source:2
# List Comprehensions
# apl-source:3
# Demonstrates: list comprehensions, filtering, conditions inline
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/33-comprehension-examples.apl
# apl-source:6

# apl-source:7
الأرقام = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# apl-source:8

# apl-source:9
print("=== قوائم الفهم (Comprehensions) ===")
# apl-source:10
print("")
# apl-source:11
print("الأصلية: " + str(الأرقام))
# apl-source:12
print("مضروبة في 2: " + str([x * 2 for x in الأرقام]))
# apl-source:13
print("الأعداد الفردية: " + str([x for x in الأرقام if x % 2 == 1]))
# apl-source:14
print("الأعداد الكبيرة (>{5}): " + str([x for x in الأرقام if x > 5]))
# apl-source:15
print("مربعات الزوجية: " + str([x * x for x in الأرقام if x % 2 == 0]))
# apl-source:16
print("")
# apl-source:17
print("--- مع النصوص ---")
# apl-source:18
الكلمات = ["apple", "banana", "cherry", "date"]
# apl-source:19
print("بالحروف الكبيرة: " + str([w.upper() for w in الكلمات]))
# apl-source:20
print("الطويلة فقط (>5): " + str([w for w in الكلمات if len(w) > 5]))
# apl-source:21
