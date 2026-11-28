
# apl-source:1
# مثال 763 — حلال بوغل
# apl-source:2
# Boggle solver
# apl-source:3
# Demonstrates: بحث عمقي، 8 اتجاهات، مجموعة زيارة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/763-boggle-solver.apl
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
# حلال بوغل: كلمات من حروف متجاورة في شبكة
# apl-source:25
# Demonstrates: بحث عمقي بثمانية اتجاهات, مجموعة زيارة, تفضيل الأطول
# apl-source:26
# لا يجوز إعادة استعمال الخلية في الكلمة الواحدة
# apl-source:27

# apl-source:28
لوحة = [["c", "a", "t"], ["d", "o", "g"], ["s", "u", "n"]]
# apl-source:29
قاموس = ["cat", "cats", "dog", "sun", "god", "act", "sat", "ton", "nut", "can", "do", "so"]
# apl-source:30

# apl-source:31
def في_القاموس(كلمة):
  # apl-source:32
  for كلمة_قاموس in قاموس:
    # apl-source:33
    if كلمة_قاموس == كلمة:
      # apl-source:34
      return True
  # apl-source:35
  return False
# apl-source:36

# apl-source:37
def ابحث(صف, عمود, كلمة, مزارة, موجودات):
  # apl-source:38
  if في_القاموس(كلمة):
    # apl-source:39
    if (كلمة in موجودات) == False:
      # apl-source:40
      موجودات.append(كلمة)
  # apl-source:41
  for دصف in [-1, 0, 1]:
    # apl-source:42
    for دعمود in [-1, 0, 1]:
      # apl-source:43
      ص = صف + دصف
      # apl-source:44
      ع = عمود + دعمود
      # apl-source:45
      if ص >= 0 and ص < 3 and ع >= 0 and ع < 3:
        # apl-source:46
        if ((ص * 10 + ع) in مزارة) == False:
          # apl-source:47
          ابحث(ص, ع, كلمة + لوحة[ص][ع], مزارة + [ص * 10 + ع], موجودات)
# apl-source:48

# apl-source:49
def كل_الكلمات():
  # apl-source:50
  موجودات = []
  # apl-source:51
  for صف in range(3):
    # apl-source:52
    for عمود in range(3):
      # apl-source:53
      ابحث(صف, عمود, لوحة[صف][عمود], [صف * 10 + عمود], موجودات)
  # apl-source:54
  return موجودات
# apl-source:55

# apl-source:56
def رتب(قائمة):
  # apl-source:57
  نسخة = قائمة
  # apl-source:58
  for ي in range(len(نسخة)):
    # apl-source:59
    for ج in range(ي + 1, len(نسخة)):
      # apl-source:60
      if نسخة[ج] < نسخة[ي]:
        # apl-source:61
        مؤقت = نسخة[ي]
        # apl-source:62
        نسخة[ي] = نسخة[ج]
        # apl-source:63
        نسخة[ج] = مؤقت
  # apl-source:64
  return نسخة
# apl-source:65

# apl-source:66
موجودات = رتب(كل_الكلمات())
# apl-source:67

# apl-source:68
تأكد_يساوي(موجودات, ["cat", "do", "dog", "god", "so", "sun", "ton"], "الكلمات السبع")
# apl-source:69
تأكد_يساوي(len(موجودات), 7, "سبع كلمات")
# apl-source:70
تأكد_يساوي("cats" in موجودات, False, "cats تحتاج s مجاورة لـt")
# apl-source:71
تأكد_يساوي("nut" in موجودات, False, "nut غير متصلة")
# apl-source:72

# apl-source:73
print("الكلمات:", موجودات)
# apl-source:74
