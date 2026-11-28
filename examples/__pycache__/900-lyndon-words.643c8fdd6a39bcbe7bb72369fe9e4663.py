
# apl-source:1
# مثال 900 — كلمات ليندون
# apl-source:2
# Lyndon words
# apl-source:3
# Demonstrates: خوارزمية دوفال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/900-lyndon-words.apl
# apl-source:6

# apl-source:7
# كلمات ليندون: الكلمات التي تسبق كل تدويراتها في الترتيب الأبجدي
# apl-source:8
# خوارزمية دوفال تولدها كلها بطول يقسم ن
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
# دوفال على الأبجدية الثنائية {0,1} للكلمات التي طولها يقسم 4
# apl-source:19
def ليندون_ثنائية(ن):
  # apl-source:20
  نتيجة = []
  # apl-source:21
  س = [-1]
  # apl-source:22
  while len(س) > 0:
    # apl-source:23
    س[len(س) - 1] = س[len(س) - 1] + 1
    # apl-source:24
    م = len(س)
    # apl-source:25
    if ن % م == 0:
      # apl-source:26
      كلمة = ""
      # apl-source:27
      for رقم in س:
        # apl-source:28
        كلمة = كلمة + str(رقم)
      # apl-source:29
      نتيجة = نتيجة + [كلمة]
    # apl-source:30
    while len(س) < ن:
      # apl-source:31
      س = س + [س[len(س) - م]]
    # apl-source:32
    while len(س) > 0 and س[len(س) - 1] == 1:
      # apl-source:33
      س = س[:len(س) - 1]
  # apl-source:34
  return نتيجة
# apl-source:35

# apl-source:36
كلمات = ليندون_ثنائية(4)
# apl-source:37
print("كلمات ليندون الثنائية التي طولها يقسم 4:", كلمات)
# apl-source:38

# apl-source:39
تأكد_يساوي(len(كلمات), 6, "ست كلمات")
# apl-source:40
تأكد_يساوي(كلمات[0], "0", "0")
# apl-source:41
تأكد_يساوي(كلمات[1], "0001", "0001")
# apl-source:42
تأكد_يساوي(كلمات[2], "0011", "0011")
# apl-source:43
تأكد_يساوي(كلمات[3], "01", "01")
# apl-source:44
تأكد_يساوي(كلمات[4], "0111", "0111")
# apl-source:45
تأكد_يساوي(كلمات[5], "1", "1")
# apl-source:46
