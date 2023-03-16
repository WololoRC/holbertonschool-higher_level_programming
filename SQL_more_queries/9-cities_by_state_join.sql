-- List all cities by citie.id, cite.name, state.name.
SELECT cities.id, cities.name, states.name FROM states, cities WHERE cities.state_id=states.id;
