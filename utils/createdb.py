#!/usr/bin/env python3

import sqlite3
import os

here = os.path.dirname(__file__)

def CreateDBTables(dbpath):
    usersSQL="""CREATE TABLE users (
                    id int, 
                    email varchar(255) not null,
                    nameDetails varchar(255),
                    PRIMARY KEY(id)
                    );
                    """

    postsSQL="""CREATE TABLE posts (
                    id int,
                    userId int not null,
                    postDate datetime,
                    postText text,
                    FOREIGN KEY(userId) REFERENCES users(id)
                    );
                    """

    likesSQL="""CREATE TABLE likes (
                    userId int not null,
                    postId int not null,
                    FOREIGN KEY(userId) REFERENCES users(id),
                    FOREIGN KEY(postId) REFERENCES posts(id)
                    );
                    """

    conn = sqlite3.connect(dbpath)

    sqls = [usersSQL, postsSQL, likesSQL]
    for sql in sqls:
        conn.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    fileDb = "file.db"
    if os.path.exists(fileDb):
        os.unlink(fileDb)
    CreateDBTables(fileDb)
