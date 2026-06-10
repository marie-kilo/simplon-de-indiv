-- Création vue
CREATE VIEW tp_and_notebook AS
SELECT n.notebook_id, n.notebook_name, t.tp_name
FROM notebook n
JOIN tp t ON n.tp_id = t.tp_id;

SELECT * FROM tp_and_notebook;