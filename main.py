from source import create_app

ENV = 'PROD'

app = create_app(ENV)

if __name__ == '__main__':
    app.run(debug=True)
   