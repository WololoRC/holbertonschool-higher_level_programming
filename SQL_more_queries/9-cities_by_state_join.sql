-- List all cities by citie.id, cite.name, state.name.
SELECT cities.id, cities.name, states.name FROM states, cities WHERE citie.state_id=state.id;
