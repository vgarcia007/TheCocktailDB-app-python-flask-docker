""" Import needed modules """
from flask import Flask, render_template
import requests
import sys
from os import environ

""" Create a Flask constructor. It takes name of the current module as the argument """
app = Flask(__name__)

""" Base urls for the cocktails api """
api_url = environ.get('API_URL') + environ.get('API_KEY') + '/'


""" Helper function to log something to console an view it with docker logs """
def console_log(text):
    print(text, file=sys.stderr)


"""Create a route decorator to tell the application,
which URL should be called for the described function and define the function """


@app.route('/')
def start_page():
    """Serve homepage template."""

    return render_template('start_page.html')


@app.route('/cocktails_by_letter/<letter>')
def cocktails_by_letter(letter):
    """List Cocktails by start letter."""

    url = api_url + 'search.php?f=' + letter
    cocktails = requests.get(url)
    cocktails_json = cocktails.json()

    if cocktails_json['drinks'] == None:
        return render_template('no-cocktails-for-letter.html', letter=letter)

    return render_template('drinks.html', cocktails=cocktails_json, current_letter=letter)


@app.route('/cocktail/<iid>')
def cocktail_by_id(iid):
    """Show cocktail details by id."""

    url = api_url + 'lookup.php?i=' + iid
    cocktails = requests.get(url).json()

    return render_template('drink-details.html', cocktail=cocktails['drinks'][0])


"""Create the main driver function """
if __name__ == '__main__':
    """call the run method"""
    app.run(host='0.0.0.0')
