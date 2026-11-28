
# apl-source:1
# مثال 2094 — دالة أكرمان لمدخلات صغيرة
# apl-source:2
# Ackermann function
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2094-ackermann-function-small-inputs.apl
# apl-source:6

# apl-source:7
# # نجرب قيما صغيرة فقط
# apl-source:8
# # الاستدعاء الذاتي المتداخل
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
def اكرمان(م, ن):
  # apl-source:19
  if م == 0:
    # apl-source:20
    return ن + 1
  # apl-source:21
  if ن == 0:
    # apl-source:22
    return اكرمان(م - 1, 1)
  # apl-source:23
  return اكرمان(م - 1, اكرمان(م, ن - 1))
# apl-source:24

# apl-source:25
تأكد_يساوي(اكرمان(0, 4), 5, "م=٠")
# apl-source:26
تأكد_يساوي(اكرمان(1, 5), 7, "م=١")
# apl-source:27
تأكد_يساوي(اكرمان(2, 3), 9, "م=٢")
# apl-source:28
تأكد_يساوي(اكرمان(3, 2), 29, "م=٣")
# apl-source:29
