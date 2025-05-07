Solar System: Wave 08!

For this activity we’ll be rejoining our Solar System groups to complete Wave 08: One-to-Many Relationships! 

The goals for this activity are to:
Add a Moon model
Create a one-to-many relationship between the Planet and Moon models 
Add nested routes for the endpoint `/planets/<planet_id>/moons` to:
Create a Moon and link it to an existing Planet record
Fetch all Moons that a Planet is associated with
To get started, each team should:
Designate who will be the initial driver
When you’re ready to switch drivers, commit and push the changes so far. The next driver should pull the changes then run any new migrations before resuming writing new code.

Once your group is set up, teams will:
Create a Moon model with attributes `size` and `description`, and at least one other attribute you choose together.
Make a foreign key connection between Planet and Moon models using `back_populates` to create a bidirectional relationship. [SQLAlchemy docs on one-to-many]
Make sure to create and run migrations as the models change, and to commit those files so your teammates can access them as well!
For testing, you may want to update the Planet’s `to_dict` function to return info about their moons, if they exist. 
Create a nested route for `/planets/<planet_id>/moons` with the POST method which allows you to add a new moon to an existing planet resource with id `<planet_id>`.
Make sure to test out your new route in a browser or Postman before continuing!
Create a nested route for `/planets/<planet_id>/moons` with the GET method which returns all moons for the planet with the id `<planet_id>`.
If you finish and have more time, take a look at what could be refactored or discuss what other nested endpoints you think would be helpful!