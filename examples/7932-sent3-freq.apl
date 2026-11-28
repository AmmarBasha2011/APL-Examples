# مثال 7932 — تكرار كل كلمة في الجملة رقم 4
# freq for sentence 4
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7932-sent3-freq.apl

# نقسم الجملة إلى كلمات
# ونعالجها حسب المطلوب

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  د = {}
  لكل ك في ن.split(" "):
    د[ك] = د.get(ك, 0) + 1
  ارجع د

تأكد_يساوي(ف("one fish two fish red fish blue fish"), {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}, "حالة 1")
تأكد_يساوي(ف("tea for two and two for tea"), {"tea": 2, "for": 2, "two": 2, "and": 1}, "حالة 2")
تأكد_يساوي(ف("red blue green red blue red"), {"red": 3, "blue": 2, "green": 1}, "حالة 3")
