
# apl-source:1
# مثال 1992 — تصنيف الأعداد وافرة أو ناقصة أو تامة
# apl-source:2
# Abundant deficient perfect classify
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1992-abundant-deficient-perfect-classify.apl
# apl-source:6

# apl-source:7
# # القواسم الحقيقية لا تشمل العدد نفسه
# apl-source:8
# # ثم نعد الأعداد الوافرة حتى 30
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def مجموع_قواسم(ن):
  # apl-source:19
  مج = 0
  # apl-source:20
  for د in range(1, ن):
    # apl-source:21
    if ن % د == 0:
      # apl-source:22
      مج = مج + د
  # apl-source:23
  return مج
# apl-source:24

# apl-source:25
def صنف(ن):
  # apl-source:26
  م = مجموع_قواسم(ن)
  # apl-source:27
  if م == ن:
    # apl-source:28
    return "perfect"
  # apl-source:29
  if م > ن:
    # apl-source:30
    return "abundant"
  # apl-source:31
  return "deficient"
# apl-source:32

# apl-source:33
تأكد_يساوي(صنف(6), "perfect", "٦")
# apl-source:34
تأكد_يساوي(صنف(28), "perfect", "٢٨")
# apl-source:35
تأكد_يساوي(صنف(12), "abundant", "١٢")
# apl-source:36
تأكد_يساوي(صنف(8), "deficient", "٨")
# apl-source:37
تأكد_يساوي(صنف(1), "deficient", "١")
# apl-source:38
عدد = 0
# apl-source:39
for ن in range(1, 31):
  # apl-source:40
  if صنف(ن) == "abundant":
    # apl-source:41
    عدد = عدد + 1
# apl-source:42
تأكد_يساوي(عدد, 5, "الوافرة حتى ٣٠")
# apl-source:43
