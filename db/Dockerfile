FROM mdillon/postgis:9.5
MAINTAINER Jonathan Meyer <jonathan.meyer@appliedis.com>

# Copy in the initial data into the postgres container init location
COPY zip_geocode.sql /docker-entrypoint-initdb.d/zip_geocode.sql

