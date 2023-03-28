DROP DATABASE IF EXISTS Tokaido;

CREATE DATABASE Tokaido
    DEFAULT CHARACTER SET = 'utf8';

USE Tokaido;

CREATE TABLE Joueur (
	j_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	j_pseudo VARCHAR(20),
	j_mdp VARCHAR(20),
	j_win INT DEFAULT 0,
	j_lose INT DEFAULT 0,
  j_position INT DEFAULT 0,
  j_couleur VARCHAR(20) DEFAULT 'NONE',
  j_money INT DEFAULT 0,
  j_point INT DEFAULT 0,
	PRIMARY KEY (j_id)
)
ENGINE=INNODB;


-- Première Pioche, ici Relais (repas)

CREATE TABLE Repas (
    id_repas INT NOT NULL,
    nom_repas VARCHAR(100),
    cout INT,
    PRIMARY KEY (id_repas)
)
ENGINE=INNODB;

-- Deuxième pioche, ici Echoppe

CREATE TABLE Echoppe (
    id_echoppe INT NOT NULL,
    nom_souvenir VARCHAR(100),
    prix INT,
    PRIMARY KEY (id_echoppe)
)
ENGINE=INNODB;

-- Troisième pioche, ici Rencontre

CREATE TABLE Rencontre (
    id_rencontre INT NOT NULL,
    nom_rencontre VARCHAR(100),
    PRIMARY KEY (id_rencontre)
)
ENGINE=INNODB;

-- Premier Inventaire, ici Echoppe

CREATE TABLE Inventaire_Echoppe (
    id_joueur INT UNSIGNED NOT NULL,
    id_item INT NOT NULL,
    CONSTRAINT pk_Inventaire_Echoppe PRIMARY KEY(id_joueur, id_item),
    CONSTRAINT fk_id_joueur FOREIGN KEY (id_joueur) REFERENCES Joueur(j_id),
    CONSTRAINT fk_id_item FOREIGN KEY (id_item) REFERENCES Echoppe(id_echoppe)
)
ENGINE=INNODB;

-- Deuxième Inventaire, ici Relais (repas)

CREATE TABLE Inventaire_Relais (
    id_perso INT UNSIGNED NOT NULL,
    id_manger INT NOT NULL,
    CONSTRAINT pk_Inventaire_Relais PRIMARY KEY(id_perso, id_manger),
    CONSTRAINT fk_id_perso FOREIGN KEY (id_perso) REFERENCES Joueur(j_id),
    CONSTRAINT fk_id_manger FOREIGN KEY (id_manger) REFERENCES Repas(id_repas)
)
ENGINE=INNODB;

-- Troisième Inventaire, ici Rencontre

CREATE TABLE Inventaire_Rencontre (
    id_voyageur INT UNSIGNED NOT NULL,
    id_qui INT NOT NULL,
    CONSTRAINT pk_Inventaire_Rencontre PRIMARY KEY(id_voyageur, id_qui),
    CONSTRAINT fk_id_voyageur FOREIGN KEY (id_voyageur) REFERENCES Joueur(j_id),
    CONSTRAINT fk_id_qui FOREIGN KEY (id_qui) REFERENCES Rencontre(id_rencontre)
)
ENGINE=INNODB;


-- Fin de la création des différentes Tables



-- Ajouts des différents items dans leur pioche respective


INSERT INTO Echoppe
VALUES (1,'Yunomi',1),(2,'Gofu',1),(3,'Koma',1),(4,'Hashi',1),(5,'Uchiwa',1),(6,'Washi',1),
        (7,'Konpeito',1),(8,'Manju',1),(9,'Kanaboto',1),(10,'Daifuku',2),(11,'Ocha',2),(12,'Sake',2),
        (13,'Sandogasa',2),(14,'Yukata',2),(15,'Furoshiki',2),(16,'geta',2),(17,'Kanzashi',2),(18,'Haori',2),
        (19,'Netsuke',2),(20,'Jubako',2),(21,'Shikki',2),(22,'Shamisen',3),(23,'Sumie',3),(24,'Ukiyoe',3);

INSERT INTO Repas
VALUES (1,'Misoshiru',1),(2,'Misoshiru',1),(3,'Misoshiru',1),(4,'Nigirimeshi',1),(5,'Nigirimeshi',1),(6,'Nigirimeshi',1),
        (7,'Dango',1),(8,'Dango',1),(9,'Dango',1),(10,'Yakitori',2),(11,'Yakitori',2),(12,'Soba',2),(13,'Soba',2),
        (14,'Sushi',2),(15,'Sushi',2),(16,'Tofu',2),(17,'Tofu',2),(18,'Tempura',2),(19,'Tempura',2),
        (20,'Unagi',3),(21,'Donburi',3),(22,'Udon',3),(23,'Fugu',3),(24,'Tai Meshi',3),(25,'Sashimi',3);

INSERT INTO Rencontre
VALUES (1,'Annaibito Rizière'),(2,'Annaibito Rizière'),(3,'Annaibito Mer'),(4,'Annaibito Mer'),(5,'Annaibito Montagne'),(6,'Annaibito Montagne'),
        (7,'Shokunin'),(8,'Shokunin'),(9,'Miko'),(10,'Miko'),(11,'Kuge'),(12,'Kuge'),(13,'Samurai'),(14,'Samurai');

