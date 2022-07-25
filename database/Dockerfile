FROM mysql:8
ENV MYSQL_ROOT_PASSWORD='admin'
COPY Database.sql /docker-entrypoint-initdb.d
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["mysqld"]
