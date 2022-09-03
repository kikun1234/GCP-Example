from flask import Flask
app = Flask(__name__)

@app.route('/')
def function():
    import pandas as pd
    from sklearn.cluster import KMeans
    df = pd.read_csv("https://gist.githubusercontent.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv")
    df = df.drop(columns={"name","horsepower"})
    df=df.astype("float64")
    kmeans = KMeans(n_clusters=5, random_state=0).fit(df)
    df['labels']=kmeans.labels_
    result = df.to_json(orient="records")
    return(result)

if __name__ == '__main__':
  app.run()