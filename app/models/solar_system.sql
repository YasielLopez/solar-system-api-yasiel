-- Complete the following setup steps of the Solar System API repo:
-- 1. Activate the virtual environment
-- 1. Create the database `solar_system_development`
--     * *Every member of the group must create the database on their computer*
-- 1. Setup the `Planet` model with the attributes `id`, `name`, and `description`, and one additional attribute
-- 1. Create a migration to add a table for the `Planet` model and then apply it. 
--     * *Confirm that the `planet` table has been created as expected in postgres*.

-- Create solar system database
CREATE DATABASE solar_system_development;

-- Create Planet model
CREATE TABLE planets(
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY ,
    name VARCHAR(30) NOT NULL,
    description TEXT NOT NULL,
    diameter_km INT NOT NULL
    );

-- Add planets data to table
INSERT INTO planets (name, description, diameter_km)
VALUES('Mercury', 'The smallest and innermost planet in the Solar System', 4879),
        ('Venus', 'Second planet from the Sun with thick atmosphere', 12104),
        ('Earth', 'Our home planet and the only known planet with life', 12742),
        ('Mars', 'The Red Planet, fourth from the Sun', 6779),
        ('Jupiter', 'The largest planet in our Solar System', 139820),
        ('Saturn', 'Known for its prominent ring system', 116460),
        ('Uranus', 'The seventh planet from the Sun', 50724),
        ('Neptune', 'The eighth and farthest planet from the Sun', 49244);

-- Check to see that table was created.
SELECT * FROM planets;

-- Run this command in postgres CLI:
--                      psql -U postgres solar_system_development < solar_system.sql
-- Make sure you are in the same folder as the file when you run this command