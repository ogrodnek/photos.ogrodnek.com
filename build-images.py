#!/usr/bin/python

import glob
import sys
import re

images = glob.glob(sys.argv[1] + "/*_1024.jpg")

header = """
{% extends "base.html" %}
{% block content %}

<div class="row set-description">
 <div class="col-sm-4">
   <h1>Header</h1>
   <p>
   blah, blah, blah, blah, blah
   </p>
 </div>
</div>
"""

footer = """
{% endblock content %}
"""

img_block="""
<div class="large-image-row">
  <div class="row">
    <div class="col-sm-12">
      <img class="img-responsive" src="{{% static '{img_path}' %}}" />
    </div>
 </div>
 <div class="row">
   <div class="col-sm-12">
     <p class="large-img-details">{desc}</p>
   </div>
 </div>
</div>
"""

print(header)

for img in images:
  m = re.search('static(/.*)', img)
  print(img_block.format(img_path=m.group(1), desc=sys.argv[2]))

print(footer)