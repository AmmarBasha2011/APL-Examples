
# apl-source:1
# مثال 1512 — صافي القيمة الحالية
# apl-source:2
# Net present value
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1512-net-present-value.apl
# apl-source:6

# apl-source:7
# نقسم كل تدفق على (1+النسبة) أس الفترة
# apl-source:8
# نقرب لأقرب جنيه
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
def صافي_القيمة(نسبة, تدفقات):
  # apl-source:19
  مجموع = 0.0
  # apl-source:20
  for ع in range(len(تدفقات)):
    # apl-source:21
    مجموع = مجموع + تدفقات[ع] / ((1 + نسبة) ** ع)
  # apl-source:22
  return int(مجموع + 0.5)
# apl-source:23

# apl-source:24
تأكد_يساوي(صافي_القيمة(0.1, [-100, 110]), 0, "تعادل")
# apl-source:25
تأكد_يساوي(صافي_القيمة(0.1, [-1000, 500, 500, 500]), 243, "ثلاث دفعات")
# apl-source:26
تأكد_يساوي(صافي_القيمة(0.0, [-50, 20, 40]), 10, "بلا خصم")
# apl-source:27
