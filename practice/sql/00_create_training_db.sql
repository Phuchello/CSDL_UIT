/* IT004 training database — original compact fixture. */
IF DB_ID(N'IT004_Training') IS NULL
    EXEC(N'CREATE DATABASE [IT004_Training]');
GO
USE IT004_Training;
GO

/* The script does not drop an existing database. Run 01_schema.sql to rebuild objects. */
