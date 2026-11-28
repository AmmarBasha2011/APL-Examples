
# apl-source:1
# مثال 1365 — تجزئة مستقرة
# apl-source:2
# Stable partition around pivot
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1365-partition-stable.apl
# apl-source:6

# apl-source:7
# نجمع الأصغر ثم الأكبر أو المساوي
# apl-source:8
# كل مجموعة تحفظ ترتيبها الأصلي
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
def جزئ(أرقام, محور):
  # apl-source:19
  صغيرة = []
  # apl-source:20
  كبيرة = []
  # apl-source:21
  for ر in أرقام:
    # apl-source:22
    if ر < محور:
      # apl-source:23
      صغيرة = صغيرة + [ر]
    # apl-source:24
    else:
      # apl-source:25
      كبيرة = كبيرة + [ر]
  # apl-source:26
  return صغيرة + كبيرة
# apl-source:27

# apl-source:28
تأكد_يساوي(جزئ([1,4,3,2,5,2], 3), [1,2,2,4,3,5], "محور ثلاثة")
# apl-source:29
تأكد_يساوي(جزئ([2,1], 2), [1,2], "عنصران")
# apl-source:30
تأكد_يساوي(جزئ([], 5), [], "فارغة")
# apl-source:31
