

CREATE TABLE IF NOT EXISTS users (
    user_id int AUTO_INCREMENT PRIMARY KEY,
    pseudo VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rankedpoints INT 
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS games(
    gameId int AUTO_INCREMENT PRIMARY KEY,
    playerId int NOT NULL,
    type VARCHAR(255) NOT NULL,
    path VARCHAR(255) NOT NULL,
    FOREIGN KEY (playerId) REFERENCES users(user_id)
) ENGINE=INNODB;
