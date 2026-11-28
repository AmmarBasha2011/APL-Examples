
# apl-source:1
# مثال 1072 — أقصر جزء غير مرتب
# apl-source:2
# Shortest unsorted continuous subarray
# apl-source:3
# Demonstrates: مقارنة بالنسخة المرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1072-shortest-unsorted.apl
# apl-source:6

# apl-source:7
# نقارن القائمة بنسختها المرتبة
# apl-source:8
# أول وآخر اختلاف يحدان الجزء المطلوب
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
def اقصر_جزء_غير_مرتب(ق):
  # apl-source:19
  م = sorted(ق)
  # apl-source:20
  اول = -1
  # apl-source:21
  اخر = -1
  # apl-source:22
  for ع in range(len(ق)):
    # apl-source:23
    if ق[ع] != م[ع]:
      # apl-source:24
      if اول == -1:
        # apl-source:25
        اول = ع
      # apl-source:26
      اخر = ع
  # apl-source:27
  if اول == -1:
    # apl-source:28
    return 0
  # apl-source:29
  return (اخر - اول) + 1
# apl-source:30

# apl-source:31
تأكد_يساوي(اقصر_جزء_غير_مرتب([2, 6, 4, 8, 10, 9, 15]), 5, "خمسة")
# apl-source:32
تأكد_يساوي(اقصر_جزء_غير_مرتب([1, 2, 3, 4]), 0, "مرتبة")
# apl-source:33
تأكد_يساوي(اقصر_جزء_غير_مرتب([1]), 0, "عنصر")
# apl-source:34
تأكد_يساوي(اقصر_جزء_غير_مرتب([2, 1]), 2, "عنصران")
# apl-source:35
