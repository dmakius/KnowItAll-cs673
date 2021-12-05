from source import create_app

ENV = 'PROD' 

app = create_app(ENV)

if __name__ == '__main__':
    if ENV == "PROD":
        app.run(debug=False)
    else:
        app.run(debug=True)