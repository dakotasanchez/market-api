#import os
#from flask import Flask, request, session, g, redirect, url_for, abort, jsonify
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models import Market

import simplejson as json
from flask import jsonify

""" CONFIG """

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:stringargs@localhost:5432/market_test'

db = SQLAlchemy(app)

""" VIEWS """

@app.route('/markets')
def hey():
    data = db.session.query(Market.market_name,
                            Market.street,
                            Market.city,
                            Market.state,
                            Market.location,
                            Market.soap).filter(Market.city == 'Portland').all()
    return jsonify(markets = data)
    """return jsonify(markets=[d.json() for d in data])"""

""" MISC """

"""
def haversine(lat1, long1, lat2, long2):

#define d2r (M_PI / 180.0)

double dlong = (long2 - long1) * d2r;
double dlat = (lat2 - lat1) * d2r;
double a = pow(sin(dlat/2.0), 2) + cos(lat1*d2r) * cos(lat2*d2r) * pow(sin(dlong/2.0), 2);
double c = 2 * atan2(sqrt(a), sqrt(1-a));
double d = 3956 * c; 
return d;
"""

""" MAIN """

if __name__ == "__main__":
    app.run(host='0.0.0.0')
