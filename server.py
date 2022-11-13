from search import Search
from wiki import Wiki
from contactus import ContactUs
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('page.html')


@app.route('/results', methods=['POST', 'GET'])
def results_web(content: str = 'web', page_count: int = 0, filter_space: str = 'default'):
    if request.method == 'GET':
        try:
            query = request.args.get('search-query')
            cl = Search(query=query, filter_str=filter_space)
            wiki_content = Wiki(query=query)

            para, img = wiki_content.data()

            if content == 'web':
                return render_template('index.html', results=cl.show_page(page_count), para=para, img=img)
            elif content == 'img':
                return render_template('index.html', results=cl.img_page(page_count))
            else:
                return render_template('404.html')
        except:
            return render_template('404.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            name = request.form.get('name')
            des = request.form.get('description')
            cont = ContactUs(email, des=des, name=name)
            cont.send()
            return redirect(url_for('home_page'))
        except:
            return render_template("404.html")

    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()


