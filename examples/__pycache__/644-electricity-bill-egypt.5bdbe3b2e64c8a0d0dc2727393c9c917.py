
# apl-source:1
# مثال 644 — فاتورة الكهرباء المنزلية
# apl-source:2
# Egypt electricity bill
# apl-source:3
# Demonstrates: شرائح، كيلوواط، فاتورة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/644-electricity-bill-egypt.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# فاتورة الكهرباء المنزلية بشرائح (تقريبية تعليمية)
# apl-source:25
# Demonstrates: شرائح استهلاك متراكمة, حساب تدريجي, خدمة عملاء
# apl-source:26
# كل شريحة لها سعرها ويحسب كل جزء بسعر شريحته
# apl-source:27

# apl-source:28
شرائح = [[50, 68], [100, 78], [200, 95], [350, 155], [650, 210], [1000, 240], [1000000000, 275]]
# apl-source:29

# apl-source:30
def فاتورة(كيلوواط):
  # apl-source:31
  قرش = 0
  # apl-source:32
  بداية = 0
  # apl-source:33
  for شريحة in شرائح:
    # apl-source:34
    نهاية = شريحة[0]
    # apl-source:35
    if كيلوواط > بداية:
      # apl-source:36
      خاضع = min(كيلوواط, نهاية) - بداية
      # apl-source:37
      قرش = قرش + خاضع * شريحة[1]
      # apl-source:38
      بداية = نهاية
  # apl-source:39
  return قرش / 100.0
# apl-source:40

# apl-source:41
تأكد_يساوي(فاتورة(30), 20.4, "ثلاثون كيلوواط")
# apl-source:42
تأكد_يساوي(فاتورة(50), 34.0, "أول شريحة كاملة")
# apl-source:43
تأكد_يساوي(فاتورة(100), 73.0, "شريحتان")
# apl-source:44
print("فاتورة 200 كيلوواط:", فاتورة(200), "جنيه")
# apl-source:45
تأكد_يساوي(فاتورة(200), 168.0, "ثلاث شرائح")
# apl-source:46
