
# apl-source:1
# مثال 1048 — جدول عدد البتات
# apl-source:2
# Counting bits table
# apl-source:3
# Demonstrates: علاقة نصف العدد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1048-count-bits-table.apl
# apl-source:6

# apl-source:7
# عدد بتات ع يساوي عدد بتات نصفه مضافاً إليه آخر بت
# apl-source:8
# فنبني الجدول في مرور واحد
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
def بتات(ن):
  # apl-source:19
  ج = [0] * (ن + 1)
  # apl-source:20
  for ع in range(1, ن + 1):
    # apl-source:21
    ج[ع] = ج[ع // 2] + (ع % 2)
  # apl-source:22
  return ج
# apl-source:23

# apl-source:24
تأكد_يساوي(بتات(5), [0, 1, 1, 2, 1, 2], "حتى خمسة")
# apl-source:25
تأكد_يساوي(بتات(0), [0], "صفر فقط")
# apl-source:26
تأكد_يساوي(بتات(8)[7], 3, "سبعة")
# apl-source:27
تأكد_يساوي(بتات(16)[15], 4, "خمسة عشر")
# apl-source:28
