CREATE DATABASE IF NOT EXISTS gestion_conges;
USE gestion_conges;

CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    post_nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    mot_de_passe VARCHAR(255),
    poste_id INT,
    manager_id INT,
    roles ENUM('employe', 'manager', 'admin')
);

CREATE TABLE postes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    descrip TEXT,
    superieur_id INT
);

CREATE TABLE conges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    utilisateur_id INT,
    date_debut DATE,
    date_fin DATE,
    motif TEXT,
    statut ENUM('en_attente', 'valide', 'rejete') DEFAULT 'en_attente'
);
    