# مثال 7972 — تكرار كل كلمة في الجملة رقم 8
# freq for sentence 8
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7972-sent7-freq.apl

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

تأكد_يساوي(ف("run run run fast fast slow"), {"run": 3, "fast": 2, "slow": 1}, "حالة 1")
تأكد_يساوي(ف("red blue green red blue red"), {"red": 3, "blue": 2, "green": 1}, "حالة 2")
تأكد_يساوي(ف("learn code learn more code more"), {"learn": 2, "code": 2, "more": 2}, "حالة 3")
