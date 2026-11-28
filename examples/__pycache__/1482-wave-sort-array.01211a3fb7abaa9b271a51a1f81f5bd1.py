
# apl-source:1
# مثال 1482 — ترتيب موجي
# apl-source:2
# Wave sort array
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1482-wave-sort-array.apl
# apl-source:6

# apl-source:7
# نبدل كل جارين عند اللزوم
# apl-source:8
# العناصر في المواقع الزوجية تكون أكبر من جيرانها
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
def رتب_موجياً(أ):
  # apl-source:19
  for ع in range(0, len(أ), 2):
    # apl-source:20
    if ع > 0 and أ[ع - 1] > أ[ع]:
      # apl-source:21
      ت = أ[ع]
      # apl-source:22
      أ[ع] = أ[ع - 1]
      # apl-source:23
      أ[ع - 1] = ت
    # apl-source:24
    if ع + 1 < len(أ) and أ[ع] < أ[ع + 1]:
      # apl-source:25
      ت = أ[ع]
      # apl-source:26
      أ[ع] = أ[ع + 1]
      # apl-source:27
      أ[ع + 1] = ت
  # apl-source:28
  return أ
# apl-source:29

# apl-source:30
def موجية(أ):
  # apl-source:31
  for ع in range(0, len(أ), 2):
    # apl-source:32
    if ع > 0 and أ[ع] < أ[ع - 1]:
      # apl-source:33
      return False
    # apl-source:34
    if ع + 1 < len(أ) and أ[ع] < أ[ع + 1]:
      # apl-source:35
      return False
  # apl-source:36
  return True
# apl-source:37

# apl-source:38
تأكد_يساوي(موجية(رتب_موجياً([1, 2, 3, 4, 5])), True, "خمسة")
# apl-source:39
تأكد_يساوي(موجية(رتب_موجياً([5, 4, 3, 2, 1, 0])), True, "تنازلي")
# apl-source:40
تأكد_يساوي(موجية(رتب_موجياً([7])), True, "وحيد")
# apl-source:41
