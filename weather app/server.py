from flask  import Flask , render_template ,request 
from weather import get_current_weather
from waitress import serve 
app=Flask(__name__)
@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html")
@app.route("/weather")
def get_weather():
    city=request.args.get("city")
    weather_data=get_current_weather(city)
    print(render_template("weather.html",title=weather_data["location"]["name"],))

if __name__=="__main__":
    serve(app,host="0.0.0.0",port=8000)
