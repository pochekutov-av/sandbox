CREATE DATABASE md
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
COMMENT ON DATABASE md IS 'The master data management database';


CREATE DATABASE md_test
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
COMMENT ON DATABASE md_test IS 'Test database for md';


\c md_test postgres;
ALTER DATABASE md_test SET TIMEZONE='UTC';


\c md postgres;
ALTER DATABASE md SET TIMEZONE='UTC';

