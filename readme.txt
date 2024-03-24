TODO list:


előre kigenerálini a meccseket sorrendben (next matches) utólag csak hozzáadni a nyerteseket és veszteseket a megfelelő meccsekhez
TBT-to be the first match, thus nobody will come to the table twice in a row
a next_matches be csak olyan meccsek lehetnek benne amiket meg is lehet jelenteni tehát egyik versenyző sem noneType
advance bracket for all round, play automatically matches with 1 competitor, and generate new matches in the next round
show rankings on the projection
show selected match at the top of the next match list on the projection
after every played match save the bracket
check competitor number in current round to assume if it is semifinal or final
add button for starting a category
create new window for the active category
create new window with active categories on tables and next matches for projecting
create a list with the category start order and present it in the projection window
double ask functions which delete data: recreate Bracket, change match result ...
logic for deciding the table side
undo
change result of a match
merge new competitor into running category
random placement seeding
calculate ranking above 4 based on the opponents rankinks
csapat pontot számolni
adatbázisba feltölteni mindent
 
Tesztelés
Tesztelni 32 emberes táblázatra


command for ui generation:

pyuic6 -o Window.py View.ui
pyuic6 -o CategoryView.py CategoryView.ui