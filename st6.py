# Step 6: Heatmap of countries vs indicators
top_bottom = pd.concat([
    df_latest.sort_values("DDI", ascending=False).head(20),
    df_latest.sort_values("DDI", ascending=True).head(20)
])
melted = top_bottom.melt(
    id_vars=["country","DDI"],
    value_vars=numeric_cols,
    var_name="Indicator",
    value_name="Score"
)
pivot = melted.pivot(index="country", columns="Indicator", values="Score")

plt.figure(figsize=(12,10))
sns.heatmap(pivot, annot=False, cmap="YlGnBu", cbar=True)
plt.title("🌍 Digital Divide Heatmap: Countries vs Indicators", fontsize=14)
plt.show()
