
# apl-source:1
# مثال 1924 — متتالية جراي
# apl-source:2
# Generate Gray code sequence
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1924-gray-code-sequence-generate.apl
# apl-source:6

# apl-source:7
# الصيغة ك xor (ك >> 1)
# apl-source:8
# نولد كل العناصر
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
def جراي(ب):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ك in range(1 << ب):
    # apl-source:21
    خرج = خرج + [ك ^ (ك >> 1)]
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
def بتات_مختلفة(أ, ب):
  # apl-source:25
  س = أ ^ ب
  # apl-source:26
  عد = 0
  # apl-source:27
  while س > 0:
    # apl-source:28
    عد = عد + (س & 1)
    # apl-source:29
    س = س >> 1
  # apl-source:30
  return عد
# apl-source:31

# apl-source:32
ج = جراي(3)
# apl-source:33
تأكد_يساوي(ج, [0, 1, 3, 2, 6, 7, 5, 4], "٣ بتات")
# apl-source:34
تأكد_يساوي(بتات_مختلفة(ج[3], ج[4]), 1, "فرق بت")
# apl-source:35
تأكد_يساوي(بتات_مختلفة(ج[7], ج[0]), 1, "دائرية")
# apl-source:36
