
# apl-source:1
# مثال 1101 — أكبر عدد بتغيير خانة
# apl-source:2
# Maximum 69 number
# apl-source:3
# Demonstrates: تغيير أول ستة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1101-max-69-number.apl
# apl-source:6

# apl-source:7
# تحويل أول ستة من اليسار إلى تسعة يعطي أكبر زيادة
# apl-source:8
# ولو لم توجد ستة بقي العدد كما هو
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
def اكبر_69(ن):
  # apl-source:19
  س = str(ن)
  # apl-source:20
  ناتج = ""
  # apl-source:21
  بدلنا = False
  # apl-source:22
  for ح in س:
    # apl-source:23
    if (ح == "6") and (بدلنا == False):
      # apl-source:24
      ناتج = ناتج + "9"
      # apl-source:25
      بدلنا = True
    # apl-source:26
    else:
      # apl-source:27
      ناتج = ناتج + ح
  # apl-source:28
  return int(ناتج)
# apl-source:29

# apl-source:30
تأكد_يساوي(اكبر_69(9669), 9969, "أول ستة")
# apl-source:31
تأكد_يساوي(اكبر_69(9996), 9999, "ستة أخيرة")
# apl-source:32
تأكد_يساوي(اكبر_69(9999), 9999, "بلا ستة")
# apl-source:33
