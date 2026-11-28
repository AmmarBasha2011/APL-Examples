# مثال 6462 — القائمة معكوسة: الكلمات ذات الطول الزوجي ثم (أول حرف كبير)
# rev of cap over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6462-words-even_len-cap-rev.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["On"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["Simple", "Code"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Five", "Four"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["Dddd", "Bb"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["Question", "Is", "That", "Be", "To", "Or", "Be", "To"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Code", "Code", "Data", "Data", "Data"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["To", "Learning", "Is", "To", "Learning"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
