
# apl-source:1
# مثال 594 — تذكرة مترو القاهرة
# apl-source:2
# Cairo metro fare
# apl-source:3
# Demonstrates: تعريفة، شرائح، محطات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/594-cairo-metro-fare.apl
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
# تذكرة مترو القاهرة حسب عدد المحطات (تعريفة مبسطة تقريبية)
# apl-source:25
# Demonstrates: شرائح أسعار, حساب مبلغ إجمالي لرحلة ذهاب وعودة
# apl-source:26
# القاعدة المفترضة هنا: حتى 9 محطات 8 جنيهات، حتى 16 عشرة، وأكثر 12
# apl-source:27

# apl-source:28
def سعر_التذكرة(محطات):
  # apl-source:29
  if محطات <= 9:
    # apl-source:30
    return 8
  # apl-source:31
  if محطات <= 16:
    # apl-source:32
    return 10
  # apl-source:33
  return 12
# apl-source:34

# apl-source:35
def تكلفة_يومية(محطات_الذهاب, أيام):
  # apl-source:36
  return سعر_التذكرة(محطات_الذهاب) * 2 * أيام
# apl-source:37

# apl-source:38
تأكد_يساوي(سعر_التذكرة(5), 8, "رحلة قصيرة")
# apl-source:39
تأكد_يساوي(سعر_التذكرة(12), 10, "رحلة متوسطة")
# apl-source:40
تأكد_يساوي(سعر_التذكرة(20), 12, "رحلة طويلة")
# apl-source:41
print("اشتراك عمل شهري (22 يوم، 14 محطة):", تكلفة_يومية(14, 22), "جنيه")
# apl-source:42
تأكد_يساوي(تكلفة_يومية(14, 22), 440, "تكلفة شهرية ذهاب وعودة")
# apl-source:43
