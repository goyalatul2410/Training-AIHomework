from flask import Flask
from apis import health_api, ping_api
from reciever import info_api


app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(health_api)
app.register_blueprint(ping_api)
app.register_blueprint(info_api)



def main():
    app.run()

if __name__ == "__main__":
    main()