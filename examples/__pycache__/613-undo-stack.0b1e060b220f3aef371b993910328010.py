
# apl-source:1
# مثال 613 — تراجع وإعادة
# apl-source:2
# Undo redo stack
# apl-source:3
# Demonstrates: تراجع، إعادة، سجل أوامر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/613-undo-stack.apl
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
# تراجع وإعادة: محرر نصوص بسجل أوامر
# apl-source:25
# Demonstrates: مكدسا تراجع وإعادة, أمر عكسي, نقطة الحفظ
# apl-source:26
# كل تعديل يسجل عكسه ليتراجع عنه بدقة
# apl-source:27

# apl-source:28
def أنشئ_محرر():
  # apl-source:29
  return {"نص": "", "تراجع": [], "إعادة": []}
# apl-source:30

# apl-source:31
def أضف(م, نص):
  # apl-source:32
  م["تراجع"].append({"نوع_العملية": "حذف", "نص": نص, "طول_قبل": len(م["نص"])})
  # apl-source:33
  م["نص"] = م["نص"] + نص
  # apl-source:34
  م["إعادة"] = []
# apl-source:35

# apl-source:36
def تراجع(م):
  # apl-source:37
  if len(م["تراجع"]) > 0:
    # apl-source:38
    أمر = م["تراجع"].pop()
    # apl-source:39
    محذوف = م["نص"][أمر["طول_قبل"]:]
    # apl-source:40
    م["نص"] = م["نص"][:أمر["طول_قبل"]]
    # apl-source:41
    م["إعادة"].append({"نص": محذوف})
# apl-source:42

# apl-source:43
def أعد(م):
  # apl-source:44
  if len(م["إعادة"]) > 0:
    # apl-source:45
    أمر = م["إعادة"].pop()
    # apl-source:46
    م["تراجع"].append({"نوع_العملية": "حذف", "نص": أمر["نص"], "طول_قبل": len(م["نص"])})
    # apl-source:47
    م["نص"] = م["نص"] + أمر["نص"]
# apl-source:48

# apl-source:49
م = أنشئ_محرر()
# apl-source:50
أضف(م, "مرحبا")
# apl-source:51
أضف(م, " ")
# apl-source:52
أضف(م, "يا عالم")
# apl-source:53
تأكد_يساوي(م["نص"], "مرحبا يا عالم", "نص كامل")
# apl-source:54
تراجع(م)
# apl-source:55
تأكد_يساوي(م["نص"], "مرحبا ", "بعد التراجع")
# apl-source:56
أعد(م)
# apl-source:57
تأكد_يساوي(م["نص"], "مرحبا يا عالم", "بعد الإعادة")
# apl-source:58
تراجع(م)
# apl-source:59
تراجع(م)
# apl-source:60
أضف(م, "-")
# apl-source:61
تأكد_يساوي(len(م["إعادة"]), 0, "تعديل جديد يمسح الإعادة")
# apl-source:62
print("النص النهائي:", م["نص"])
# apl-source:63
