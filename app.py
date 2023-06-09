import flask
from flask import Flask
from ayomide_sdk.rest import Client

app = Flask(__name__)

version = "v2"
api_key = "API-KEY"
client = Client(version=version, api_key=api_key)


@app.route("/")
def home():
    return f'<h3>Welcome to my minimal flask app built on ayomide-sdk</h3> <ol> <li>Pypi link : https://pypi.org/project/ayomide-sdk/</li> <li>Github Repository : https://github.com/Alsaheem/ayomide-sdk</li> <li>Linkedin : https://www.linkedin.com/in/adebisi-ayomide/</li> </ol> <h3>Quick Links</h3> <ol> <li><a href="http://127.0.0.1:5000/quotes">http://127.0.0.1:5000/quotes</a></li> <li><a href="http://127.0.0.1:5000/movies">http://127.0.0.1:5000/movies</a></li> <li><a href="http://127.0.0.1:5000/quote/5cd95395de30eff6ebccde57">http://127.0.0.1:5000/quote/5cd95395de30eff6ebccde57</a></li> <li><a href="http://127.0.0.1:5000/movie/5cd95395de30eff6ebccde57">http://127.0.0.1:5000/movie/5cd95395de30eff6ebccde57</a></li> </ol>'


@app.route("/quotes")
def quotes():
    sdk_resp = client.quote.get(filters={"limit": "10"})  # using pagination and filters
    sdk_api_status = sdk_resp.get("status")
    data = {}
    if sdk_api_status != 200:
        pass
    else:
        data = sdk_resp["json"]
    response = flask.jsonify({"success": True, "data": data})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, sdk_api_status


@app.route("/movies")
def movies():
    sdk_resp = client.movie.get()
    sdk_api_status = sdk_resp.get("status")
    data = {}
    if sdk_api_status != 200:
        pass
    else:
        data = sdk_resp["json"]
    response = flask.jsonify({"success": True, "data": data})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, sdk_api_status


@app.route("/movie/<movie_id>")
def single_movie(movie_id=None):
    movie_id = movie_id
    if movie_id == None:
        response = flask.jsonify(
            {"success": False, "message": "Movie id cannot be empty"}
        )
        return response, 400
    else:
        sdk_resp = client.movie.get(params={"id": f"{movie_id}"})
        sdk_api_status = sdk_resp.get("status")
        data = {}
        if sdk_api_status != 200:
            pass
        else:
            data = sdk_resp["json"]
            response = flask.jsonify({"success": True, "data": data})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response, sdk_api_status


@app.route("/quote/<quote_id>")
def single_quote(quote_id=None):
    quote_id = quote_id
    if quote_id == None:
        response = flask.jsonify(
            {"success": False, "message": "Movie id cannot be empty"}
        )
        return response, 400
    else:
        sdk_resp = client.movie.get(params={"id": f"{quote_id}"})
        sdk_api_status = sdk_resp.get("status")
        data = {}
        if sdk_api_status != 200:
            pass
        else:
            data = sdk_resp["json"]
            response = flask.jsonify({"success": True, "data": data})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response, sdk_api_status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
