from src.apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="192.168.251.2", port=5005, debug=True)
