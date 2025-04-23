-- Complete the following setup steps of the Solar System API repo:
-- 1. Activate the virtual environment
-- 1. Create the database `solar_system_development`
--     * *Every member of the group must create the database on their computer*
-- 1. Setup the `Planet` model with the attributes `id`, `name`, and `description`, and one additional attribute
-- 1. Create a migration to add a table for the `Planet` model and then apply it. 
--     * *Confirm that the `planet` table has been created as expected in postgres*.

CREATE DATABASE solar_system_development;

CREATE TABLE planet(
    'id' INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY ,
    'name' VARCHAR(30) NOT NULL,
    'description' TEXT NOT NULL,
    'diameter_km' INT NOT NULL
    );

INSERT INTO planet
VALUES(
    (1, "Mercury", "The smallest and innermost planet in the Solar System", 4879),
    (2, "Venus", "Second planet from the Sun with thick atmosphere", 12104),
    (3, "Earth", "Our home planet and the only known planet with life", 12742),
    (4, "Mars", "The Red Planet, fourth from the Sun", 6779),
    (5, "Jupiter", "The largest planet in our Solar System", 139820),
    (6, "Saturn", "Known for its prominent ring system", 116460),
    (7, "Uranus", "The seventh planet from the Sun", 50724),
    (8, "Neptune", "The eighth and farthest planet from the Sun", 49244),
);

-- Check to see that table was created.
SELECT * from planet;