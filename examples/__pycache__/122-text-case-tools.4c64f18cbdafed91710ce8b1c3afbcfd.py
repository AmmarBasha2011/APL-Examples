
# apl-source:1
# مثال 122 — أدوات الحالة والفحص في النصوص
# apl-source:2
# Case and inspection string tools
# apl-source:3
# Demonstrates: علوي، سفلي، بداية، نهاية، تقليم، استبدال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/122-text-case-tools.apl
# apl-source:6

# apl-source:7
نص = "  Ammar Programming Language  "
# apl-source:8
print("الأصل: [", نص, "]")
# apl-source:9
print("مقلم: [", نص.strip(), "]")
# apl-source:10
print("علوي:", نص.upper())
# apl-source:11
print("سفلي:", نص.lower())
# apl-source:12
print("يبدأ بـ Ammar؟", نص.strip().startswith("Ammar"))
# apl-source:13
print("ينتهي بـ Language؟", نص.strip().endswith("Language"))
# apl-source:14
print("استبدال:", نص.strip().replace("Programming", "Coding"))
# apl-source:15
print("عدد حرف a:", نص.count("a"))
# apl-source:16
