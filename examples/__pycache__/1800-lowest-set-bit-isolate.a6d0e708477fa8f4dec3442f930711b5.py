
# apl-source:1
# مثال 1800 — عزل أدنى بت مضاء
# apl-source:2
# Isolate lowest set bit
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1800-lowest-set-bit-isolate.apl
# apl-source:6

# apl-source:7
# الإشارة السالبة تقلب البتات
# apl-source:8
# النتيجة قوة اثنين
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
def أدنى_بت(ن):
  # apl-source:19
  return ن & (-ن)
# apl-source:20

# apl-source:21
تأكد_يساوي(أدنى_بت(12), 4, "اثنا عشر")
# apl-source:22
تأكد_يساوي(أدنى_بت(7), 1, "سبعة")
# apl-source:23
تأكد_يساوي(أدنى_بت(64), 64, "قوة")
# apl-source:24
تأكد_يساوي(أدنى_بت(10), 2, "عشرة")
# apl-source:25
