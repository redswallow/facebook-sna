import tornado
import os
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("facebook_api_key", help="your Facebook application API key",
       default="1374846899425612")
define("facebook_secret", help="your Facebook application secret",
       default="7cafc9eb807cb67f717b08775cb56559")
tornado.options.parse_command_line()

settings = dict(
            cookie_secret="facebooksna",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            facebook_api_key=options.facebook_api_key,
            facebook_secret=options.facebook_secret,
            #ui_modules={"Post": PostModule},
            debug=True,
            autoescape=None,
        )
