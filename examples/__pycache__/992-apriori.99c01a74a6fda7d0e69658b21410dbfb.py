
# apl-source:1
# مثال 992 — خوارزمية أبريوري
# apl-source:2
# Apriori algorithm
# apl-source:3
# Demonstrates: تقليم بعتبة الدعم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/992-apriori.apl
# apl-source:6

# apl-source:7
# خوارزمية أبريوري: الأصناف والأزواج المتكررة في سلة مشتريات
# apl-source:8
# عتبة الدعم تقلم المرشحين جيلاً بعد جيل
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
سلال = [["milk", "bread"], ["milk", "diaper", "beer"], ["milk", "bread", "diaper"], ["bread", "diaper"], ["milk", "bread", "beer"]]
# apl-source:19
أصناف = ["beer", "bread", "diaper", "milk"]
# apl-source:20
عتبة = 2
# apl-source:21

# apl-source:22
def يحتوي(سلة, صنف):
  # apl-source:23
  for عنصر in سلة:
    # apl-source:24
    if عنصر == صنف:
      # apl-source:25
      return 1
  # apl-source:26
  return 0
# apl-source:27

# apl-source:28
def دعم1(صنف):
  # apl-source:29
  عد = 0
  # apl-source:30
  for سلة in سلال:
    # apl-source:31
    if يحتوي(سلة, صنف) == 1:
      # apl-source:32
      عد = عد + 1
  # apl-source:33
  return عد
# apl-source:34

# apl-source:35
def دعم2(أ, ب):
  # apl-source:36
  عد = 0
  # apl-source:37
  for سلة in سلال:
    # apl-source:38
    if (يحتوي(سلة, أ) == 1) and (يحتوي(سلة, ب) == 1):
      # apl-source:39
      عد = عد + 1
  # apl-source:40
  return عد
# apl-source:41

# apl-source:42
متكررة = []
# apl-source:43
for صنف in أصناف:
  # apl-source:44
  if دعم1(صنف) >= عتبة:
    # apl-source:45
    متكررة = متكررة + [صنف]
# apl-source:46

# apl-source:47
أزواج = 0
# apl-source:48
دعم_خبز_حليب = 0
# apl-source:49
for i in range(len(متكررة)):
  # apl-source:50
  for j in range(i + 1, len(متكررة)):
    # apl-source:51
    د = دعم2(متكررة[i], متكررة[j])
    # apl-source:52
    if د >= عتبة:
      # apl-source:53
      أزواج = أزواج + 1
      # apl-source:54
      if (متكررة[i] == "bread") and (متكررة[j] == "milk"):
        # apl-source:55
        دعم_خبز_حليب = د
# apl-source:56

# apl-source:57
تأكد_يساوي(len(متكررة), 4, "أربعة أصناف متكررة")
# apl-source:58
تأكد_يساوي(دعم1("bread"), 4, "دعم الخبز")
# apl-source:59
تأكد_يساوي(دعم1("beer"), 2, "دعم المشروب")
# apl-source:60
تأكد_يساوي(أزواج, 4, "أربعة أزواج متكررة")
# apl-source:61
تأكد_يساوي(دعم_خبز_حليب, 3, "دعم الزوج الأشهر")
# apl-source:62
