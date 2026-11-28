# مثال 7922 — تكرار كل كلمة في الجملة رقم 3
# freq for sentence 3
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7922-sent2-freq.apl

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

تأكد_يساوي(ف("apl code is easy code is fun"), {"apl": 1, "code": 2, "is": 2, "easy": 1, "fun": 1}, "حالة 1")
تأكد_يساوي(ف("we love data and data loves us"), {"we": 1, "love": 1, "data": 2, "and": 1, "loves": 1, "us": 1}, "حالة 2")
تأكد_يساوي(ف("in the end the end is the start"), {"in": 1, "the": 3, "end": 2, "is": 1, "start": 1}, "حالة 3")
