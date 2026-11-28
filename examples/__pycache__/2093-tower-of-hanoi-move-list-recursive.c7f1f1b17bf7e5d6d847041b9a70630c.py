
# apl-source:1
# مثال 2093 — أبراج هانوي قائمة الحركات
# apl-source:2
# Tower of Hanoi moves
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2093-tower-of-hanoi-move-list-recursive.apl
# apl-source:6

# apl-source:7
# # الدالة تستدعي نفسها مرتين
# apl-source:8
# # عدد الحركات 2 أس ن ناقص 1
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
def حركات(ن, من, الى, عبر):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return []
  # apl-source:21
  return حركات(ن - 1, من, عبر, الى) + [[من, الى]] + حركات(ن - 1, عبر, الى, من)
# apl-source:22

# apl-source:23
تأكد_يساوي(حركات(2, "A", "C", "B"), [["A", "B"], ["A", "C"], ["B", "C"]], "قرصان")
# apl-source:24
تأكد_يساوي(len(حركات(3, "A", "C", "B")), 7, "ثلاثة")
# apl-source:25
تأكد_يساوي(len(حركات(10, "A", "C", "B")), 1023, "عشرة")
# apl-source:26
تأكد_يساوي(حركات(0, "A", "C", "B"), [], "بلا أقراص")
# apl-source:27
