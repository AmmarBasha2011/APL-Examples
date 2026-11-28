# مثال 8002 — تكرار كل كلمة في الجملة رقم 11
# freq for sentence 11
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8002-sent10-freq.apl

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

تأكد_يساوي(ف("red blue green red blue red"), {"red": 3, "blue": 2, "green": 1}, "حالة 1")
تأكد_يساوي(ف("nile river nile delta river"), {"nile": 2, "river": 2, "delta": 1}, "حالة 2")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), {"bread": 3, "milk": 2, "eggs": 1}, "حالة 3")
