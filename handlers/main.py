from handlers.base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render('base.html')
