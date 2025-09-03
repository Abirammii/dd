# Step 7: K-Means Clustering
X = df_latest[numeric_cols]
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df_latest['cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(10,7))
scatter = plt.scatter(X_pca[:,0], X_pca[:,1], c=df_latest['cluster'], cmap='viridis', s=50)
plt.title("🌍 Country Clusters Based on Digital Divide Indicators", fontsize=14)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(*scatter.legend_elements(), title="Cluster")
plt.show()
