# importing 'app' variable from __init__
from myApp import app

# True when script is run directly using python
if __name__ == '__main__':
    app.run(debug=True)
