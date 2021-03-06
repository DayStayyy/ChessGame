CREATE TABLE IF NOT EXISTS users (
    user_id int AUTO_INCREMENT PRIMARY KEY,
    pseudo VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rankedpoints INT DEFAULT 0
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS games(
    gameId int AUTO_INCREMENT PRIMARY KEY,
    playerId int NOT NULL,
    type VARCHAR(255) NOT NULL,
    path VARCHAR(255) NOT NULL,
    turn int NOT NULL DEFAULT 1,
    FOREIGN KEY (playerId) REFERENCES users(user_id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS score (
    game_id int,
    result VARCHAR(255) NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games(gameId)
    
)  ENGINE=INNODB;