
# apl-source:1
# مثال 4835 — مبلغ بعد فائدة مركبة 8%
# apl-source:2
# Compound balance at 8 percent (integer)
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4835-compound-8.apl
# apl-source:6

# apl-source:7
# كل سنة نضيف الفائدة على الرصيد
# apl-source:8
# القسمة صحيحة
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
def ف(م, س):
  # apl-source:19
  for ي in range(س):
    # apl-source:20
    م = م + م * 8 // 100
  # apl-source:21
  return م
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(1000, 1), 1080, "حالة 1")
# apl-source:24
تأكد_يساوي(ف(1000, 5), 1467, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(500, 3), 629, "حالة 3")
# apl-source:26
تأكد_يساوي(ف(20000, 2), 23328, "حالة 4")
# apl-source:27
