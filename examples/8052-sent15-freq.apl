# مثال 8052 — تكرار كل كلمة في الجملة رقم 16
# freq for sentence 16
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8052-sent15-freq.apl

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

تأكد_يساوي(ف("stars and moon and stars again"), {"stars": 2, "and": 2, "moon": 1, "again": 1}, "حالة 1")
تأكد_يساوي(ف("left right left left right"), {"left": 3, "right": 2}, "حالة 2")
تأكد_يساوي(ف("apl code is easy code is fun"), {"apl": 1, "code": 2, "is": 2, "easy": 1, "fun": 1}, "حالة 3")
