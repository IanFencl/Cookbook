from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=dam0GPOAvVI
#https://stackoverflow.com/questions/44941757/sqlalchemy-exc-operationalerror-sqlite3-operationalerror-no-such-table