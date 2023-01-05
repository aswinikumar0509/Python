def is_automorphic_number(n):
    return str(n**2).endswith(str(n))
print(is_automorphic_number(5))