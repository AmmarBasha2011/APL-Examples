
# apl-source:1
# مثال 123 — التقسيم والدمج
# apl-source:2
# Split and join pipelines
# apl-source:3
# Demonstrates: تقسيم، ضم، فرز، عكس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/123-text-split-join.apl
# apl-source:6

# apl-source:7
سطر = "تفاح,موز,برتقال,عنب,فراولة"
# apl-source:8
فواكه = سطر.split(",")
# apl-source:9
print("القائمة:", فواكه)
# apl-source:10

# apl-source:11
فواكه.sort()
# apl-source:12
print("مرتبة:", " | ".join(فواكه))
# apl-source:13

# apl-source:14
فواكه.reverse()
# apl-source:15
print("معكوسة:", "-".join(فواكه))
# apl-source:16

# apl-source:17
جملة = ["APL", "لغة", "عربية"]
# apl-source:18
print("جملة:", " ".join(جملة))
# apl-source:19
