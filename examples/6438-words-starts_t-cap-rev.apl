# مثال 6438 — القائمة معكوسة: الكلمات التي تبدأ بـ t ثم (أول حرف كبير)
# rev of cap over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6438-words-starts_t-cap-rev.apl

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
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["The", "The"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Three", "Two"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["The", "That", "To", "To"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["Think", "To", "To"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
