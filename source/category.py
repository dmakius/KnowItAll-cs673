from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from . import db

category = Blueprint("category", __name__)

@category.route('/category/select', methods=['GET', 'POST'])
def mycategory(self):
    if request.method == 'POST':
        print(self.select_category)
        return redirect(url_for("view.game"))
        # if request.form.get('geography'):
        #     select_category = "geography"
        #     return select_category, redirect(url_for("view.game"))
        # elif request.form.get('art'):
        #     select_category = "art"
        #     return select_category
        # elif request.form.get('computer-science'):
        #     select_category = "computer-science"
        #     return select_category
        # elif request.form.get('science'):
        #     select_category = "science"
        #     return select_category
        # elif request.form.get('mythology'):
        #     select_category = "mythology"
        #     return select_category
        # elif request.form.get('TV-shows'):
        #     select_category = "TV-shows"
        #     return select_category
        # elif request.form.get('movie'):
        #     select_category = "movie"
        #     return select_category