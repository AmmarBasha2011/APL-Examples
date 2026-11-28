# مثال 6446 — القائمة معكوسة: الكلمات التي تبدأ بـ t ثم (أول حرف)
# rev of first over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6446-words-starts_t-first-rev.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: القائمة معكوسة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    لو ك[0] == "t":
      ر = ر + [ك[0]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["t", "t"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["t", "t"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t", "t", "t", "t"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["t", "t", "t"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
