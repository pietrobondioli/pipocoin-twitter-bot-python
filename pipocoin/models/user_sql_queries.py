SQL_FETCH_ALL_USERS = """SELECT *
                          FROM user;"""

SQL_FETCH_USER_BY_ID = """SELECT *
                            FROM user
                            WHERE twitter_id=?;"""

SQL_FETCH_USER_BY_NAME = """SELECT *
                              FROM user
                              WHERE user_name=?;"""

SQL_CREATE_NEW_USER = """INSERT INTO
                          user(twitter_id, user_name, balance)
                          VALUES(?, ?, ?)"""

SQL_DELETE_USER = """DELETE
                      FROM user
                      WHERE twitter_id=?"""

SQL_INCREASE_USER_BALANCE_BY_ID = """UPDATE user
                                  SET balance = (balance + ?)
                                  WHERE twitter_id=?;"""

SQL_INCREASE_USER_BALANCE_BY_NAME = """UPDATE user
                                    SET balance = (balance + ?)
                                    WHERE user_name=?;"""

SQL_DECREASE_USER_BALANCE_BY_ID = """UPDATE user
                                  SET balance = (balance - ?)
                                  WHERE twitter_id=?;"""

SQL_DECREASE_USER_BALANCE_BY_NAME = """UPDATE user
                                    SET balance = (balance - ?)
                                    WHERE user_name=?;"""
