
# apl-source:1
# مثال 1307 — تدوير القائمة
# apl-source:2
# Rotate list to the right by k
# apl-source:3
# Demonstrates: تدوير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1307-rotate-list-right.apl
# apl-source:6

# apl-source:7
# نأخذ k بباقي القسمة على الطول
# apl-source:8
# ونقص الذيل ونضعه أمام الرأس
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def دور_يمين(قيم, ك):
  # apl-source:19
  if len(قيم) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ك = ك % len(قيم)
  # apl-source:22
  if ك == 0:
    # apl-source:23
    return list(قيم)
  # apl-source:24
  return قيم[-ك:] + قيم[:-ك]
# apl-source:25

# apl-source:26
تأكد_يساوي(دور_يمين([1,2,3,4,5], 2), [4,5,1,2,3], "اثنان")
# apl-source:27
تأكد_يساوي(دور_يمين([0,1,2], 4), [2,0,1], "أكبر من الطول")
# apl-source:28
تأكد_يساوي(دور_يمين([1,2], 0), [1,2], "صفر")
# apl-source:29
تأكد_يساوي(دور_يمين([], 3), [], "فارغة")
# apl-source:30
