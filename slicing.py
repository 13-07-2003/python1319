s = " soham anand bedadur"

print(f"Original String: '{s}'")
print(f"Total Length: {len(s)}")

#  Positive to Positive 
print(" Positive to Positive ")
print(f"1. {s[1:6]}")    # 'soham'
print(f"2. {s[7:12]}")   # 'anand'
print(f"3. {s[13:20]}")  # 'bedadur'
print(f"4. {s[1:12]}")   # 'soham anand'
print(f"5. {s[0:1]}")    # ' ' empty space

#  Negative to Positive 
print("\n Negative to Positive ")
print(f"1. {s[-7:20]}")  # 'bedadur'
print(f"2. {s[-13:12]}") # 'anand'
print(f"3. {s[-19:6]}")  # 'soham'
print(f"4. {s[-20:12]}") # 'soham anand'
print(f"5. {s[-13:20]}") # 'anand bedadur'

#  Positive to Negative 
print("\n Positive to Negative ")
print(f"1. {s[1:-14]}")  # 'soham'
print(f"2. {s[7:-8]}")   # 'anand'
print(f"3. {s[13:-1]}")  # 'bedadu' 
print(f"4. {s[1:-8]}")   # 'soham anand'
print(f"5. {s[0:-1]}")   # ' soham anand bedadu'

#  Negative to Negative 
print(" Negative to Negative" )
print(f"1. {s[-7:-1]}")  # 'bedadu'
print(f"2. {s[-13:-8]}") # 'anand'
print(f"3. {s[-19:-14]}")# 'soham'
print(f"4. {s[-20:-8]}") # 'soham anand'
print(f"5. {s[-20:-14]}")# 'soham'
