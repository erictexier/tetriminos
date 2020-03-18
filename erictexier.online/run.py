import sys
from base_site import create_app
app = create_app()

if __name__ == '__main__':
    import os
    # context = ('localhost.crt', 'localhost.key')
    # app.run(debug=True, port=5000, ssl_context=context)
    # When running locally, disable OAuthlib's HTTPs verification.
    # ACTION ITEM for developers:
    #     When running in production *do not* leave this option enabled.
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Specify a hostname and port that are set as a valid redirect URI
    # for your API project in the Google API Console.
    # app.run('localhost', 5000, debug=True)
    if "--setup" in sys.argv:
        from base_site import db
        app.app_context().push()
        db.create_all()
        db.session.commit()
        print("Database tables created")
    else:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        app.run(debug=True)
