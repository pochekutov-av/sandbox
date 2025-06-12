CREATE DATABASE md
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10
    IS_TEMPLATE = False;
COMMENT ON DATABASE md IS 'The master data management database';

\c md postgres;
ALTER DATABASE md SET TIMEZONE='UTC';


CREATE DATABASE test_md
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10
    IS_TEMPLATE = False;
COMMENT ON DATABASE md_test IS 'Test database for md';

\c test_md postgres;
ALTER DATABASE test_md SET TIMEZONE='UTC';