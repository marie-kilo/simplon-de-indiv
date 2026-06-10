-- tp
CREATE TABLE tp (
    tp_id SERIAL PRIMARY KEY,
    tp_name VARCHAR(50) NOT NULL
);

-- notebook
CREATE TABLE notebook (
    notebook_id SERIAL PRIMARY KEY,
    tp_id INT REFERENCES tp(tp_id),
    notebook_name VARCHAR(100) NOT NULL
);

INSERT INTO tp (tp_name) VALUES ('tp1'), ('tp2');

-- Insertion 
INSERT INTO notebook (tp_id, notebook_name) VALUES
(1, '0_sql_intro_northwind.ipynb'),
(1, '1_rapatrier_et_filtrer.ipynb'),
(1, '2_exercices.ipynb'),
(1, '3_corriges.ipynb'),
(2, '0_jointures_aggregation_sets.ipynb'),
(2, '1_exercices_jointures_aggregation_sets.ipynb'),
(2, '2_corriges.ipynb'); 

