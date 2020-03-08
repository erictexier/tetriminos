from base_site import create_app
app = create_app()

if __name__ == '__main__':
    # context = ('localhost.crt', 'localhost.key')
    # app.run(debug=True, port=8080, ssl_context=context)
    app.run(debug=True)
