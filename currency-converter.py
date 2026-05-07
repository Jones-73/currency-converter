def usd_to_ksh(amount_usd, rate=133):
    return amount_usd * rate

def ksh_to_usd(amount_ksh, rate=133):
    return amount_ksh / rate

print("250 USD =", usd_to_ksh(250), "KSH")
print("33,250 KSH =", round(ksh_to_usd(33250), 2), "USD")
