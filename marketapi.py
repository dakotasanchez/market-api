from flask import Flask, jsonify, request
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
from models import Market
from operator import itemgetter
import math

import simplejson as json

""" CONFIG """

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost:5432/markets'

db = SQLAlchemy(app)

""" VIEWS """

@app.route('/api/v1/markets')
def markets():
    x = request.args.get('x')
    y = request.args.get('y')
    dist = request.args.get('dist')

    """ Spherical Law of Cosines Formula """

    clause = """3959 * acos(cos(radians(:lat)) * cos(radians(y)) * cos(radians(x)
    - radians(:long)) + sin(radians(:lat)) * sin(radians(y))) < :dist"""

    query = db.session.query(Market.fmid,
                            Market.market_name,
                            Market.website,
                            Market.x,
                            Market.y).filter(clause).params(lat=y, long=x, dist=dist)

    results = [u._asdict() for u in query.all()]

    for row in results:
        row['distance'] = distance(x, y, row['x'], row['y'])

    sorted_results = sorted(results, key=itemgetter('distance'))

    return jsonify(markets = sorted_results)

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

@app.route('/api/v1/market')
def market():
    fmid = request.args.get('id')

    data = db.session.query(Market.city,
                            Market.credit,
                            Market.facebook,
                            Market.fmid,
                            Market.location,
                            Market.x,
                            Market.y,
                            Market.market_name,
                            Market.organic,
                            Market.other_media,
                            Market.season_1_date,
                            Market.season_1_time,
                            Market.sfmnp,
                            Market.snap,
                            Market.state,
                            Market.street,
                            Market.twitter,
                            Market.update_time,
                            Market.website,
                            Market.wic,
                            Market.wic_cash,
                            Market.zipcode).filter(Market.fmid == fmid).first()
    return jsonify(market = data)


def distance(my_long, my_lat, market_long, market_lat):
    my_long = float(my_long)
    my_lat = float(my_lat)
    market_long = float(market_long)
    market_lat = float(market_lat)

    return 3959 * math.acos(math.cos(math.radians(my_lat)) \
            * math.cos(math.radians(market_lat)) \
            * math.cos(math.radians(market_long) \
            - math.radians(my_long)) + math.sin(math.radians(my_lat)) \
            * math.sin(math.radians(market_lat)))


""" MAIN """

if __name__ == "__main__":
    app.run(host='0.0.0.0')
