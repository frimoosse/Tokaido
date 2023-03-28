<<<<<<< HEAD


-- ajout d'une carte à l'inventaire

INSERT INTO inventaire_x    -- avec x l'inventaire en question
VALUES (id,'nom');          -- on parcourira la bdd pioche pour retrouver l'id du joueur et le nom de l'item que l'on donnera ici



-- fin de la partie, on vide les inventaires

=======


-- ajout d'une carte à l'inventaire

INSERT INTO inventaire_x    -- avec x l'inventaire en question
VALUES (id,'nom');          -- on parcourira la bdd pioche pour retrouver l'id du joueur et le nom de l'item que l'on donnera ici



-- fin de la partie, on vide les inventaires

>>>>>>> 8008152d17c955aa3226d660de11c9d3ce1422be
DELETE FROM inventaire_x ; -- supprime l'entièreté de ce qui est présent dans l'inventaire (id comme les noms des items)