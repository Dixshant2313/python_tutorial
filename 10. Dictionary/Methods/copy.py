d = {10:100,20:200,30:300,4:400}
new_d = d.copy()
print(f"Before copy: {new_d}")

new_d[10]=150
print(d)
print(f"After copying: {new_d}")

# returns a shallow copy