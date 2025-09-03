# Step 8: Simulate +20% mobile internet
df_sim = df_latest.copy()
df_sim["IT.CEL.SETS.P2"] = np.minimum(df_sim["IT.CEL.SETS.P2"] * 1.2, 1.0)
df_sim["DDI_new"] = df_sim[numeric_cols].mean(axis=1)

df_compare = df_latest[["country","DDI"]].merge(df_sim[["country","DDI_new"]], on="country")
df_compare["Change"] = df_compare["DDI_new"] - df_compare["DDI"]
df_compare.sort_values("Change", ascending=False).head(10)
