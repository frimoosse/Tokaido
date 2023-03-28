<<<<<<< HEAD
-- Active: 1678537758458@@127.0.0.1@3306@tokaido


-- Requête de début de partie

INSERT INTO joueur
VALUES ('pseudo','mdp',NULL,nb_win,nb_lose,NULL,0,'couleur'); -- tout ce qui n'est pas null ou 0 sera ajouté via python en début de partie




-- Requêtes pendant la partie

UPDATE joueur 
SET j_position = x; -- le x sera la valeur de la position, dont le calcul sera fait sur Python

UPDATE joueur 
SET j_money = x; -- idem pour l'argent

UPDATE joueur 
SET j_points = x; -- idem pour les points




-- Requêtes de fin de partie

UPDATE joueur
SET J_win = x; -- calcul des points par Python, +1 si win, +0 si lose avec x nb de partie gagné

UPDATE joueur
=======
-- Active: 1678537758458@@127.0.0.1@3306@tokaido


-- Requête de début de partie

INSERT INTO joueur
VALUES ('pseudo','mdp',NULL,nb_win,nb_lose,NULL,0,'couleur'); -- tout ce qui n'est pas null ou 0 sera ajouté via python en début de partie




-- Requêtes pendant la partie

UPDATE joueur 
SET j_position = x; -- le x sera la valeur de la position, dont le calcul sera fait sur Python

UPDATE joueur 
SET j_money = x; -- idem pour l'argent

UPDATE joueur 
SET j_points = x; -- idem pour les points




-- Requêtes de fin de partie

UPDATE joueur
SET J_win = x; -- calcul des points par Python, +1 si win, +0 si lose avec x nb de partie gagné

UPDATE joueur
>>>>>>> 8008152d17c955aa3226d660de11c9d3ce1422be
SET j_lose = x; -- calcul des points par Python, +1 si lose, +0 si win avec x nb de partie perdue