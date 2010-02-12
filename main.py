#!/usr/bin/env python

#
#  computersays.net
#
#  Copyright (c) 2010, Boris Bluntschli <boris@bluntschli.ch>
#  Copyright (c) 2010, Daniel Gasienica <daniel@gasienica.ch>
#  All rights reserved.
#

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import random


class MainHandler(webapp.RequestHandler):    
    def get(self):
        answer = "yes" if random.random() > 0.5 else "no"
        self.response.out.write("Computer says %s." % answer)


def main():
    application = webapp.WSGIApplication([("/", MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == "__main__":
    main()
