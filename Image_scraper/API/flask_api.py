from flask import Flask, request, Response
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from main import save_images_from_google
app = Flask(__name__)
@app.route('/scrape', methods=['GET'])
def scrape_images():
    query = request.args.get('query')
    if not query:
        return Response("Missing query parameter", status=400, mimetype='text/plain')
    try:
        count = save_images_from_google(query)
        return Response(f"Saved {count} images in 'Images/' folder.", status=200, mimetype='text/plain')
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500, mimetype='text/plain')
if __name__ == '__main__':
    app.run(debug=True)