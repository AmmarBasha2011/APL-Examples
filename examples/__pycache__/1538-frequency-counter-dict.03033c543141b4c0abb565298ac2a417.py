
# apl-source:1
# مثال 1538 — عداد التكرار
# apl-source:2
# Frequency counter dictionary
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1538-frequency-counter-dict.apl
# apl-source:6

# apl-source:7
# نستخدم get بقيمة افتراضية صفر
# apl-source:8
# نزيد العداد عند كل ظهور
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
def عدّاد(أ):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    عد[ع] = عد.get(ع, 0) + 1
  # apl-source:22
  return عد
# apl-source:23

# apl-source:24
تأكد_يساوي(عدّاد(["a", "b", "a"]), {"a": 2, "b": 1}, "حروف")
# apl-source:25
تأكد_يساوي(عدّاد([]), {}, "فارغ")
# apl-source:26
تأكد_يساوي(عدّاد([1, 1, 1]), {1: 3}, "أرقام")
# apl-source:27
