# pip install waitress
# this is waitress_server.py
from waitress import serve
 
# under cmsimde import fossilapp
import fossilapp
 
# run cmsimde dynamic site with production waitress
serve(fossilapp.app, host='0.0.0.0', port=5000, url_scheme='https')