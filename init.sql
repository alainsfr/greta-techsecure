CREATE TABLE IF NOT EXISTS filiales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ville VARCHAR(100) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    responsable VARCHAR(100) NOT NULL,
    employes INT NOT NULL,
    ip VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telephone VARCHAR(50),
    message TEXT NOT NULL,
    date_envoi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertion des 3 filiales initiales de la maquette
INSERT INTO filiales (ville, adresse, responsable, employes, ip) VALUES
('Paris', '102 Avenue des Champs-Élysées, 75008 Paris', 'Jean Dupont', 85, '192.168.1.1'),
('Lyon', '15 Rue de la République, 69002 Lyon', 'Sophie Martin', 42, '192.168.2.1'),
('Marseille', '45 Quai du Port, 13002 Marseille', 'Marc Durand', 28, '192.168.3.1');