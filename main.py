from website import create_app

app = create_app()

# only run in this file and not when imported 
if __name__ == '__main__':
    app.run(debug=True)
