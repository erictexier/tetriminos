from base_site import create_app
app = create_app()

if __name__ == '__main__':
    # context = ('localhost.crt', 'localhost.key')
    # app.run(debug=True, port=8080, ssl_context=context)
    # When running locally, disable OAuthlib's HTTPs verification.
    # ACTION ITEM for developers:
    #     When running in production *do not* leave this option enabled.
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Specify a hostname and port that are set as a valid redirect URI
    # for your API project in the Google API Console.
    # app.run('localhost', 8080, debug=True)
    app.run(debug=True)
