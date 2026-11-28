
# apl-source:1
# مثال 1822 — عدد البتات المضاءة لكل عدد
# apl-source:2
# Counting bits table up to n
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1822-counting-bits-up-to-n.apl
# apl-source:6

# apl-source:7
# عدد بتات ن = عدد بتات ن/2 + آخر بت
# apl-source:8
# نملأ الجدول تدريجياً
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
def جدول_البتات(ن):
  # apl-source:19
  ج = [0]
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    ج.append(ج[ك >> 1] + (ك & 1))
  # apl-source:22
  return ج
# apl-source:23

# apl-source:24
تأكد_يساوي(جدول_البتات(5), [0, 1, 1, 2, 1, 2], "خمسة")
# apl-source:25
تأكد_يساوي(جدول_البتات(2), [0, 1, 1], "اثنان")
# apl-source:26
تأكد_يساوي(جدول_البتات(8)[8], 1, "ثمانية")
# apl-source:27
