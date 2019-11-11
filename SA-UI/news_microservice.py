import pandas as pd
from flask import *
from flask_cors import CORS, cross_origin
import uuid
# from cheroot import wsgi

app = Flask(__name__)
CORS(app)

@app.route("/summary_page", methods=['POST'])
def summary():
    score_dict = {'Brexit': 53, 'US China Trade War': 53, 'Iran Sanctions': 52, 'Boeing Crisis': 53, 'Hong Kong Protests': 52}
    picture_dict = {'Brexit': 'boris', 'US China Trade War': 'trump', 'Iran Sanctions': 'sanctions', 'Boeing Crisis': 'boeing', 'Hong Kong Protests': 'hkprotest'}
    topic = request.json['data']
    article_summary = pd.read_csv('csv/topic_summary.csv')
    positive_summary = pd.read_csv('csv/positive.csv')
    negative_summary = pd.read_csv('csv/negative.csv')
    print(topic)
    summary = article_summary[article_summary['group'].str.contains(topic, case=False)]['summary'].iat[0]
    group = article_summary[article_summary['group'].str.contains(topic, case=False)]['group'].iat[0]
    positive = positive_summary[positive_summary['group'].str.contains(topic, case=False)]['summary'].iat[0]
    negative = negative_summary[negative_summary['group'].str.contains(topic, case=False)]['summary'].iat[0]
    picture = picture_dict[group]
    score = score_dict[group]
    print(summary)
    output = [group,summary, picture, positive, negative, score]
    print(output)
    return jsonify(output) #return jsonified output back to the UI

if __name__ == "__main__":
        app.run(threaded=True, debug=True)

