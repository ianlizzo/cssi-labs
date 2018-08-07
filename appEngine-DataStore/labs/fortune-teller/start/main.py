
import webapp2
import jinja2
import os
import random


def get_fortune():
    fortune_list=['You will win a million dollars',
                  'Something cool will happen to you',
                  'You will have a successful career',
                  'You will die'
                 ]
    random_fortune = random.choice(fortune_list)
    return(random_fortune)


jinja_current_directory = jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/fortune_start.html")
        self.response.write(start_template.render())
    def post(self):
        random_fortune = get_fortune()
        user_astro_sign = self.request.get("user_astrological_sign")
        my_dict = {"the_fortune": random_fortune, "the_astro_sign": user_astro_sign}
        results_template = jinja_current_directory.get_template("templates/fortune_results.html")
        self.response.write(results_template.render(my_dict))

app = webapp2.WSGIApplication([
    ('/predict', FortuneHandler),
], debug=True)
