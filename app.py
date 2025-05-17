import feedparser
from flask import Flask, render_template

app = Flask(__name__)
ARY_FEED = "https://arynews.tv/feed/"

@app.route('/')
def new_feed():
  feed = feedparser.parse(ARY_FEED)
  first_article = feed['entries'][0]
  return render_template('index.html', article=first_article)



if __name__ == "__main__":
    app.run(debug=True)
