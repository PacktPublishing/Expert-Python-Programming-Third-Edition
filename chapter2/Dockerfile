# Let's define base image.
# "python" is official Python image.
# The "slim" versions are sensible starting
# points for other lightweight Python-based images
FROM python:3.7-slim

# In order to keep image clean let's switch
# to selected working directory. "/app/" is
# commonly used for that purpose.
WORKDIR /app/

# These are our static files copied from
# project source tree to the current working
# directory.
COPY static/ static/

# We would run "python -m http.server" locally
# so lets make it an entry point.
ENTRYPOINT ["python3.7", "-m", "http.server"]

# We want to serve files from static/ directory
# on port 80 by default so set this as default arguments
# of the built-in Python HTTP server
CMD ["--directory", "static/", "80"]
