
# apl-source:1
# مثال 1717 — عدد نقلات برج هانوي
# apl-source:2
# Tower of Hanoi move count
# apl-source:3
# Demonstrates: تكرار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1717-tower-of-hanoi-move-count.apl
# apl-source:6

# apl-source:7
# نقل ن-1 قرصاً مرتين وقرص واحد
# apl-source:8
# نتحقق من الصيغة 2^ن - 1
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
def نقلات(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return 0
  # apl-source:21
  return 2 * نقلات(ن - 1) + 1
# apl-source:22

# apl-source:23
تأكد_يساوي(نقلات(1), 1, "قرص")
# apl-source:24
تأكد_يساوي(نقلات(3), 7, "ثلاثة")
# apl-source:25
تأكد_يساوي(نقلات(10), 1023, "عشرة")
# apl-source:26
تأكد_يساوي(نقلات(6), 63, "الصيغة")
# apl-source:27
