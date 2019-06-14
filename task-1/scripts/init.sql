CREATE DATABASE knights;
use knights;

CREATE TABLE names (
  id int PRIMARY KEY,
  name VARCHAR(20),
  age int
);

INSERT INTO names
  (id, name, age)
VALUES
  (1, 'Vasanth', 21),
  (2, 'Vanan', 23),
  (3, 'Mathi', 24);