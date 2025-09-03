# Step 2: World Bank Indicators for Digital Divide
indicators = {
    "IT.NET.USER.ZS": "Internet users (% population)",
    "IT.NET.BBND.P2": "Fixed broadband subscriptions (per 100 people)",
    "IT.CEL.SETS.P2": "Mobile subscriptions (per 100 people)",
    "SE.ADT.LITR.ZS": "Adult literacy rate (%)",
    "SE.SEC.ENRR": "Secondary school enrollment (%)",
    "NY.GDP.PCAP.CD": "GDP per capita (context)"
}

print("Indicators for DDI project:")
for code, desc in indicators.items():
    print(f"{code} → {desc}")
