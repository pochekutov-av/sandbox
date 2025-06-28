CREATE DATABASE site01
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10
    IS_TEMPLATE = False;
COMMENT ON DATABASE site01 IS 'The site 01 database';


\c site01 postgres;
ALTER DATABASE site01 SET TIMEZONE='UTC';


CREATE DATABASE test_site01
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10
    IS_TEMPLATE = False;
COMMENT ON DATABASE site01_test IS 'Test database for site01';


\c test_site01 postgres;
ALTER DATABASE site01_test SET TIMEZONE='UTC';
